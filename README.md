# Hero
The article [here](https://medium.com/@estretyakov/the-ultimate-async-setup-fastapi-sqlmodel-alembic-pytest-ae5cdcfed3d4) gives a detailed description of developing an asynchronous web app with FastAPI and SQLModel. testing the database and API routes are covered using the Pytest library.

## Dependencies
Here is a short description of python packages used in the article (just to make a whole picture to save your time):

1. [Poetry](https://python-poetry.org) - is a tool for dependency management and packaging in Python. It allows you to
   declare the libraries your project depends on and it will manage (install/update) them for you;
2. [FastAPI](https://fastapi.tiangolo.com) - is a modern, fast (high-performance), web framework for building APIs with
   Python 3.6+ based on standard Python type hints;
3. [Pydantic](https://pydantic-docs.helpmanual.io) - Data validation and settings management using Python type hinting;
4. [SQLAlchemy](https://www.sqlalchemy.org) - SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that
   gives application developers the full power and flexibility of SQL;
5. [SQLModel](https://sqlmodel.tiangolo.com) - SQLModel is a library for interacting with SQL databases from Python
   code, with Python objects;
6. [Alembic](https://alembic.sqlalchemy.org/en/latest/) - Alembic is a lightweight database migration tool for usage
   with the SQLAlchemy Database Toolkit for Python.

---
<br/><br/>
## Deployment
start database container: 
```console
docker run --name heroes-pg -d \
   -e POSTGRESQL_USERNAME=hero \
   -e POSTGRESQL_PASSWORD=heroPass123 \
   -e POSTGRESQL_DATABASE=heroes_db \
   -p 5432:5432 \
   bitnami/postgresql:13
```

build the app container:
```console
docker build -t app-hero .
```
install jq:
```console
sudo apt install jq
```
And this command to start app: 
```console
docker run --name app-hero -d \
   -e POSTGRES_USERNAME=hero \
   -e POSTGRES_PASSWORD=heroPass123 \
   -e POSTGRES_DATABASE=heroes_db \
   -e POSTGRES_HOST=$(docker inspect heroes-pg | jq -r .[0].NetworkSettings.IPAddress) \
   -p 8080:80 \
   app-hero:latest
```
- `POSTGRES_HOST` - is the IP address of the database container
<br/>

>view the app [here](http://localhost:8080/docs)

---
<br/><br/>
## (SAST) SonarQube
create network:
```console
docker network create neetSonar
```
create postgres container:
```console
docker run --name postgres -d \
   -e POSTGRES_USER=root \
   -e POSTGRES_PASSWORD=Test12345 \
   -p 5434:5434 \
   --network neetSonar \
   postgres
```
create sonarqube container:
```console
docker run --name sonarqube -d \
   -e sonar.jdbc.username=root \
   -e sonar.jdbc.password=Test12345 \
   -e sonar.jdbc.url=jdbc:postgresql://postgres/postgres \
   -p 9000:9000 \
   --network neetSonar \
   sonarqube
```
create an alias:
```console
alias sonar-scanner='docker run --rm \
   --network neetSonar \
   -v "$(pwd):/usr/src" \
   sonarsource/sonar-scanner-cli'
```
on your host machine, change the permissions of the current directory:
```console
chmod 777 "$(pwd)"
```
run the the scanner:
```console
### THIS IS AN EXAMPLE ONLY ### DO NOT PASTE THIS ###
sonar-scanner \
   -Dsonar.projectKey={YOUR PROJECT} \
   -Dsonar.sources=. \
   -Dsonar.host.url=https://{YOUR SONARQUBE URL} \
   -Dsonar.login={YOUR PROJECT TOKEN}
```

---
<br/><br/>
## (DAST) OWASP ZAP
```console
docker run -t owasp/zap2docker-stable zap-baseline.py -t "http://$(docker inspect app-hero | jq -r .[0].NetworkSettings.IPAddress):8080"
```
view alerts:
- https://www.zaproxy.org/docs/alerts/10049

