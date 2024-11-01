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