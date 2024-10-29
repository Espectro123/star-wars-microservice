# Star wars microservice

This microservice get Star Wars character data from the SWAPI, sorts the characters by name, and provides a /sorted-people endpoint to access the sorted data. 

## Runing the microservice localy
```
pip install -r requirements.txt
python -m src.infrastructure.api.server
```
Go to http://127.0.0.1:5000/sorted-people to access the endpoint. You should see the logs (INFO) on the terminal

## Running the microservice in the docker container
```
docker build -t star-wars-microservice
docker run -p 5000:5000 star-wars-microservice
```

Go to http://127.0.0.1:5000/sorted-people to access the endpoint. You should see the logs (INFO) on the terminal

## Deploy the service to a kubernetes cluster (minikube)
```
minikube start
```

```
docker build -t star-wars-microservice .
kubectl apply -f k8s/star_wars_deployment.yaml
kubectl apply -f k8s/star_wars_service.yaml
minikube service star-wars-microservice-service
```

```
minikube stop
```

Click on the link shown on the URL column and add /sorted-people at the end of the route in the browser



