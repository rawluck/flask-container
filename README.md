
# Containerized Flask App with CI/CD 

A Containerized Flask Hello World App using Docker and CI/CD unit tests using Travis-CI

The flask app is run from `app.py` there an test in `test/test_app.py` which checks the contents to verify the server is up and responding correctly.

The test is run using Travis CI. Tavis also auto deploys the containter to docker hub registry using `.travis/deploy_dockerhub.sh` and `.tavis/deploy_heroku.sh` auto deploys it to heroku.

Therefore whenever code is pushed to the Github Repo Tavis CI runs the Unit Test, updates the docker registry container and deploys that container to Heroku.

[DEMO](https://rawluck.herokuapp.com/) | [Docker Registry](https://hub.docker.com/r/rawluck/flask-container)


## Deployment

Assuming you have [Docker up and running](https://docs.docker.com/get-started/).  
Simply run: 
```bash
  docker run -p 5000:5000 --rm -it rawluck/flask-container:latest
```

  
## Build Locally

Clone the project

```bash
  git clone https://github.com/rawluck/flask-container
```

Go to the project directory

```bash
  cd flask-container
```

Build 

```bash
  docker build -t flask-container .
```

Start the container

```bash
  docker run -p 5000:5000 --rm -it flask-container
```

  
