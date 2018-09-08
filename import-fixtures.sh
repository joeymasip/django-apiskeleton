#!/bin/sh

# To dump a file from the ddbb
# python manage.py dumpdata apiapp.User --indent 4 > users.json

python manage.py loaddata users
