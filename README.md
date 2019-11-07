This is a skeleton of the Django project. Including:
* Django REST framework
* Celery
* Redis as a celery broker 
* Memcached
* bunch of linters
* pytest

Rename `project_name` where necessary on your real project name.

The application requires a PostgreSQL and Redis services.
Fist of all you need to define the environment variables from the `example.env` file according to your environment.
As one of the options you can create local `.env` file and run `docker-compose up --build`.

To start the project, you need to install dependencies from the `requirements.txt` file and start the server using the `uwsgi --ini uwsgi.ini` command or use the Docker image of the application from the registry of the project.

Use `make` commands to run linters, tests with coverage report and another features (see `Makefile`).