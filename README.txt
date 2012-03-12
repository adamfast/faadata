*NOTE*: The April 5, 2012 cycle of FADDS has moved to a new format, breaking these importers. I will update them when I get the time (or it becomes a blocker to something I need) but in the meantime would absolutely accept a pull request if you're so inclined.

This project provides Django models and simple import scripts to load data provided by the Federal Aviation Administration.

Sub-apps:
  aircraft      Store / import data from the public Aircraft Registry (http://www.faa.gov/licenses_certificates/aircraft_certification/aircraft_registry/releasable_aircraft_download/)
  airports      Store / import data from the FADDS "APT" database - includes airport facilities, runways, attendance hours and remarks specific to those three items. This app is in a "pre-beta" state, the parsers are there to break everything apart but no models exist to store the data and the import process isn't done yet, either.
  awoses      Store / import data from the FADDS "AWOS" database - this lists all "automated weather observation stations" with their locations, codes, and phone numbers.

Installation:
  Add faadata.aircraft to INSTALLED_APPS
  manage.py aircraft_import --path=/path/to/AR-folder/ will then import all the aircraft registrations
  manage.py airport_import --path=/path/to/fadds/ will import all airports, runways, remarks, and attendance schedules. There is not-yet exposed granularity in the import to select which of those you want imported in the management command itself.
  manage.py awos_import --path=/path/to/fadds/ will import all automated weather observation stations
  manage.py fix_import --path=/path/to/fadds/ will import all fixes (note: a "fix" is a location used by pilots flying under Instrument Flight Rules. It is not a "physical" place just a set of pronounceable characters mapping to a latitude/longitude.)

As an extra bonus, the import-airspace-shapes.sh script will populate a database with geometry for US restricted airspace. It doesn't use Django. Sources are the shapefiles in FADDS and the SoaringWeb OpenAir files at http://soaringweb.org/Airspace/NA/HomePage.html


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
