# powerplant-coding-challenge 

## Solution by Alejandro Mata

Inside the folder `alejandro_mata_solution` there's a dockerfile that will easily run the flask app and expose the enpdpoint. 

### Run the solution

1. Go to the folder containing the docker file.
 ```bash
cd alejandro_mata_solution
 ```
 2. Build the docker image
 ```bash
 docker build -t power-plant-alejandro .
 ```


3. Run it, mapping the container port 8888 to a local port
```bash
docker run -p 8888:8888
```

4. Access the endpoint via POST (using curl, postman or something similar) at `localhost:8888/productionplan`. 

## How the solution works, algorithm review

I decided to use an iterative approach, filling the demand with the cheapest energy sources first and then adding the more expensive ones. However, a problem arises when we have a remainer smaller than the minimum production for the next plant in line.</br>
For example, if at some moment need to generate 50MWh more, and the cheapest remaining plant has a `pmin` of 100MWh, we have to work around that excess. What I came with is a best-effort excess management algorithm; therefore we will produce `pmin` with the cheapest plant remaining and substract the excess from the previous one.
</br>
If the previous one is a wind turbine or doesn't have enough `pmax` to cover the difference, we can't simply substract it, so we will accept the excess and display a warning.
This is not a perfect solution, but it works for the vast majority of possible scenarios. If you want to check a situation in which it will happen, you can use `payload_with_excess.json` and check it out.
