from flask import Flask, request, jsonify

app = Flask(__name__)

# Makes easier getting the fuel cost from the powerplant type
powerplant_fue_dict = {
    "gasfired": "gas(euro/MWh)",
    "turbojet": "kerosine(euro/MWh)",
    "windturbine": 0
}

# For health checks
@app.route('/')
def hello_world():
    return 'Testing endpoint', 200 

@app.route('/productionplan', methods=['POST'])
def production_plan():
    # Get the payload from the request
    payload = request.get_json()
    
    # If we don't get all of this fields, we consider the request invalid
    required_fields = ['load', 'fuels', 'powerplants']
    missing = [field for field in required_fields if field not in payload]
    if missing:
        return jsonify({'error': f'Missing fields: {missing}'}), 400
    
    # Extract the data
    load = payload['load']
    fuels = payload['fuels']
    powerplants = payload['powerplants']

    # Process plants gets everything done.
    production = process_plants(load, fuels, powerplants)
    return jsonify(production), 200

# Calculates the cost of production of a plant
def get_cost_of_production(plant, fuels, fuel_key):
    if plant['type'] == 'windturbine':
        return 0
    
    return fuels[fuel_key] / plant['efficiency']

# What we will do is the following:
# 1. Get the cost per megawatt produced (cost of Mwh cosumed/efficiency) for each plant
# 1. Rank the powerplants by cost.
# 2. For each one: Is the load smaller than pmin? In that case, we'll do the pmin and
# substract the excess from the previous one (i hope this doesn't happen with renewables... probably
# throw an error?)
# 3. Is the load smaller than pmax? In that case, produce the load and we're done. Again I hope
# this doesn't happen with renewables.
# 4. If the load is bigger than pmax, continue with the next powerplant substracting the pmax from the remainer

def process_plants(load, fuels, powerplants):
    for plant in powerplants:
         fuel_key = powerplant_fue_dict[plant['type']]
         plant['cost'] = get_cost_of_production(plant, fuels, fuel_key)

         if plant['type'] == 'windturbine':
             plant['pmax'] = plant['pmax'] * fuels['wind(%)']/100

    plants_sorted = sorted(powerplants, key=lambda x: x['cost'])

    remainer = load

    production = []

    for plant in plants_sorted:
        if remainer <= 0:
            production.append({'name': plant['name'], 'p': 0.0})

        elif remainer <= plant['pmin']:
            production = subtract_min_from_previous(production, plant['pmin'],remainer)
            production.append({'name': plant['name'], 'p': float(plant['pmin'])})
            remainer = 0
        
        elif remainer <= plant['pmax']:
            production.append({'name': plant['name'], 'p': float(remainer)})
            remainer = 0

        else:
            production.append({'name': plant['name'], 'p': float(plant['pmax'])})
            remainer -= plant['pmax']

    return production
            
def subtract_min_from_previous(production, pmin, remainer):
    # In the case that we need an additional plant but it's pmin is bigger than the remainer,
    # we will substract the difference from the previous plant. It's not perfect (we could see
    # if we have more expensive plants with pmin smaller, therefore cheaper) but it's something.
    differece = pmin - remainer
    production[-1]['p'] -= differece

    return production
