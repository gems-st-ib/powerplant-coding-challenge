from flask import Flask, request, jsonify

app = Flask(__name__)

powerplant_fue_dict = {
    "gasfired": "gas(euro/MWh)",
    "turbojet": "kerosine(euro/MWh)",
    "windturbine": 0
}

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
    
    load = payload['load']
    fuels = payload['fuels']
    powerplants = payload['powerplants']

    production = process_plants(load, fuels, powerplants)

    return jsonify(production), 200

def get_cost_of_production(plant, fuels, fuel_key):
    if plant['type'] == 'windturbine':
        return 0
    
    return fuels[fuel_key] / plant['efficiency']

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
            production.append({'name': plant['name'], 'p': plant['pmin']})
            remainer -= plant['pmin']
        
        elif remainer <= plant['pmax']:
            production.append({'name': plant['name'], 'p': remainer})
            remainer = 0

        else:
            production.append({'name': plant['name'], 'p': plant['pmax']})
            remainer -= plant['pmax']

    return production
            



# What we will do is the following:
# 1. Get the cost per megawatt produced (cost of Mwh cosumed/efficiency)
# 1. Rank the powerplants by cost.
# 2. For each one. Is the load smaller than pmin? In that case, we'll do the pmin and
# substract from the previous one (i hope this doesn't happen with renewables... probably
# throw an error?)
# 3. Is the load smaller than pmax? In that case, produce the load and we're done. Again I hope
# this doesn't happen with renewables.
# 4. If the load is bigger than pmax, continue with the next powerplant substracting the pmax.