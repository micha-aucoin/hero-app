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
And this command to start container: `docker run -d -p "8080:80" --name hero-app ghcr.io/micha-aucoin/hero-app:<sha-identity>`

### kubernetes
   - [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/) - download the Kubernetes command line interface on local machine to communicate with cluster
   - download kubeconfig file from cloud provider and and save it to the $KUBECONFIG environment variable: `export KUBECONFIG=~/Downloads/kubedonfig.yaml`
   - 

### Tekton
   - [Tekton Pipeline](https://tekton.dev/docs/pipelines/install/) - install Tekton Pipelines onto the Kubernetes cluster
   - [Tekton Triggers](https://tekton.dev/docs/triggers/install/) - install Tekton Triggers onto the Kubernetes cluster
   - [tkn](https://tekton.dev/docs/cli/) - intall Tekton CLI on local machine
