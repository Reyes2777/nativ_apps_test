# Nativ Apps Test

Service for course manager.

## Table of Contents

* [Contributing](#markdown-header-contributing)
  * [Installation](#markdown-header-installation)
  * [Requirent managent](#markdown-header-requirements-management)
  * [Precommit](#markdown-header-precommit)
  * [Run in local development environment](#markdown-run-in_local-development-environment)
  * [Testing](#markdown-header-testing)
  * [Releasing new version](#markdown-header-releasing-new-version)


## Contributing

### Installation

1. Clone the repo: `git clone git@github.com:Reyes2777/nativ_apps_test.git`
2. We recommend use virtualenv for the dependencies management, you have two options:
   - virtualenv: `virtualenv ryuk -p $(which python3.10)`
   - virtualenvwrapper: `mkvirtualenv ryuk -p $(which python3.10) -a .`
3. Install dev requirements: `pip install -r requirements_dev.txt`
4. Run `pre-commit install`.
5. Give executable permissions to the files for the precommit config: `chmod +x run_tests.sh run_xenon.sh`

### Requirements management

There are three requirements files:

1. *requirements_dev.txt* for development.
1. *requirements.txt* for stages and production.

**Please, don't use `pip freeze > requirements[_dev].txt` so we have a cleaner requirements files. Add specific python lib manually instead.**

### Precommit

This project uses precommit lib to check several things before make the commit. These things are:

1. Check and fix (if it can be done) end of file, double quote, detect private key, detect aws credentials, trailing whitespaces
1. Check code style (pep8).
1. Check cyclomatic complexity. If there are one greater than 20 (D), it's going to fail (this is temporary, the idea is to have a complexity number lower than 11, it's mean between A and B).

If any of these checks fail, the commit cannot be done and it's necessary to fix it.

### Run in local development environment


1. Replace in *.env* variables to local DB postgrest:
    ####
        DB_NAME=test
        DB_USER=jreyes
        DB_PASSWORD=reyes2777
        DB_HOST=db
        DB_PORT=5432
2. Export enviroments to enviroment `export $(cat .env | sed -e /^$/d -e /^#/d | xargs)`
3. Run `python manage makemigrations`
3. You should has installed Docker and run  `docker-compose up --build -d` to first initialized proyect
4. run  `docker ps ` and show the next content:

        CONTAINER ID   IMAGE                   COMMAND                  CREATED         STATUS                          PORTS                    NAMES
        5cbef8d630fd   nativ_apps_test_web     "python manage.py ru…"   29 hours ago    Up About a minute               0.0.0.0:8000->8000/tcp   nativ_apps_test_web_1
        d237a533a099   postgres:13.10-alpine   "docker-entrypoint.s…"   29 hours ago    Up About a minute               0.0.0.0:5432->5432/tcp   nativ_apps_test_db_1
5. Run `docker-exec nativ_apps_test_web /bin/sh`
6. In the terminal execute migrations with `python manage migrate`
7. In the browser open `http//:localhost:8000/courses`


### Testing

### Documentation
Show how use appliction User in file Demo.mov in this project

### Releasing new version
