# powerplant-coding-challenge


This readme fine explain how to install and test the solution given for the power-plant-coding-challenge.

## Repository

The code con be found on this url:

https://github.com/AdAM-TMC/powerplant-coding-challenge/tree/master

You can clone it by typing:
```
git clone git@github.com:AdAM-TMC/powerplant-coding-challenge.git
```

## Installing the application

This app is built using python, so python needs to be installed on your local machine. Also, poetry is needed for installing dependencies. Docker also would be needed for building and launch the container.

## Launch using docker (recommended)

First for building the image, sitting on the root folder of the project, type:
```
docker build -t code-challenge .
```

For running a container, type:
```
docker run -d -p 8888:8888 code-challenge
```

## Launch locally using poetry

Install the pyproject.toml dependencies:

```
poetry install
```

Activate the virtual environment created:

```
poetry shell
```

Launch the application with any of these commands:

```
python -m uvicorn app.app.main:app --port 8888
```

```
poetry run uvicorn app.app.main:app --host 127.0.0.1 --port 8888
```

```
uvicorn app.app.main:app --host 127.0.0.1 --port 8888
```

## Accesing the api

You can reach the deployed api swagger by accessing the url:

http://localhost:8888/docs

there you can find and empty example request.

The required endpoint can be reached on:

http://localhost:8888/api/productionplan/


### Contact info

Any doubt or question can be addressed to antonio.deantonio@tmceurope.com.


