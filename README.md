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

## Deployment
start database container: 
```
$ docker run --name heroes-pg -d \
   -e POSTGRESQL_USERNAME=hero \
   -e POSTGRESQL_PASSWORD=heroPass123 \
   -e POSTGRESQL_DATABASE=heroes_db \
   -p 5432:5432 \
   bitnami/postgresql:13
```
---
And this command to start app: 
```
$ docker run --name app-hero -d \
   -e POSTGRES_USERNAME=hero \
   -e POSTGRES_PASSWORD=heroPass123 \
   -e POSTGRES_DATABASE=heroes_db \
   -p 8080:80 \
   ghcr.io/micha-aucoin/hero-app:sha-1319c62
```
>view the app [here](http://localhost:8080/docs)

