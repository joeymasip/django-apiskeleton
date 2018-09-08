Docker environment for Django 1.11, Django REST Framework and Django JWT
========================================================================

# How to run

Run `docker-compose up -d`. This will initialise and start all the containers, then leave them running in the background.

## Services exposed outside your environment

You can access your application via **`127.0.0.1:8000`**, if you're running the containers directly.

## Hosts within your environment

You'll need to configure your application to use any services you enabled:

Service|Hostname |Port number
-------|---------|-----------
django |django   |8000
mysql  |mysql    |8306


# Installation:

Type `docker-compose exec django bash` in your shell to enter the python django shell.

Now run the migrations like so

`python manage.py makemigrations` and `python manage.py migrate`

or

`bash install.sh`

**Note:** If it's the first time you're running the migrations and your app is not working in your browser, try `docker-compose stop` and `docker-compose up -d` again. This is due to Django trying to execute the app without the ddbb created yet. It should now work.

## Django fixtures:

Type `docker-compose exec django bash` in your shell to enter the python django shell.

Then run the fixtures like so

`python manage.py loaddata users`

or

`bash import-fixtures.sh`

## PyCharm configuration:
  * Run `docker-compose up -d` and in **Settings - Project: xxxx - Project interpreter** 
    * Add remote interpreter (cog)
      * type: Docker compose
      * service: django
  * **Run - Edit configurations** add a new **Django server**:
    * Host: 0.0.0.0
    * Port: 8000
    * Python interpreter: The remote python added in previous step...


# Docker compose cheatsheet

**Note:** you need to cd first to where your docker-compose.yml file lives.

  * Start containers in the background: `docker-compose up -d`
  * Start containers on the foreground: `docker-compose up`. You will see a stream of logs for every container running.
  * Stop containers: `docker-compose stop`
  * Kill containers: `docker-compose kill`
  * View container logs: `docker-compose logs`
  * Execute command inside of container: `docker-compose exec SERVICE_NAME COMMAND` where `COMMAND` is whatever you want to run. Examples:
    * Shell into the django container, `docker-compose exec django bash`
    * Open a mysql shell, `docker-compose exec mysql mysql -uroot -pCHOSEN_ROOT_PASSWORD`

# Docker general cheatsheet

**Note:** these are global commands and you can run them from anywhere.

  * To clear containers: `docker rm -f $(docker ps -a -q)`
  * To clear images: `docker rmi -f $(docker images -a -q)`
  * To clear volumes: `docker volume rm $(docker volume ls -q)`
  * To clear networks: `docker network rm $(docker network ls | tail -n+2 | awk '{if($2 !~ /bridge|none|host/){ print $1 }}')`