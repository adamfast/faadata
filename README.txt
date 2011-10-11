This project provides Django models and simple import scripts to load data provided by the Federal Aviation Administration.

Sub-apps:
  aircraft      Store / import data from the public Aircraft Registry (http://www.faa.gov/licenses_certificates/aircraft_certification/aircraft_registry/releasable_aircraft_download/)
  airports      Store / import data from the FADDS "APT" database - includes airport facilities, runways, attendance hours and remarks specific to those three items. This app is in a "pre-beta" state, the parsers are there to break everything apart but no models exist to store the data and the import process isn't done yet, either.

Installation:
  Add faadata.aircraft to INSTALLED_APPS
  Set settings.FAA_AIRCRAFT_DB_PATH to the path to the registry file downloaded from the above link
  export your DJANGO_SETTINGS_MODULE
  python aircraft/load.py will then import all the aircraft registrations

As an extra bonus, the import-airspace-shapes.sh script will populate a database with geometry for US restricted airspace. 

Detailed usage notes:

Postgres:

Create a clean database named "faadata"
Do the postgis spatial stuff to add functions, CRS, etc. See
https://docs.djangoproject.com/en/dev/ref/contrib/gis/install/#spatialdb-template


Django setup:

Get faadata and faddsdata from github
Put those two python libraries in your PYTHONPATH
python manage.py syncdb
python manage.py runserver
test the server
  http://127.0.0.1:8000/airports/ should be empty
  http://127.0.0.1:8000/airports/SQL/ should return a 404 saying "No airport found matching the query"

Data import:

Download and unpack the FADDS zip
Disable DEBUG in settings.py
python manage.py fadds_import --faddspath=$HOME/src/faa-postgis/Oct20-Dec15/
  takes a few minutes
Re-enable DEBUG in settings.py
python manage.py runserver
test the server
  http://127.0.0.1:8000/airports/ should show page 1 of 996 or so with 20 airports
  http://127.0.0.1:8000/airports/SQL/ should show data for San Carlos