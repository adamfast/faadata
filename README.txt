faadata has been checked with FADDS data from the cycle effective 2017-08-17.

This project provides Django models and simple import scripts to load data provided by the Federal Aviation
Administration about the National Airspace System.

Sub-apps:
  aircraft      Store / import data from the public Aircraft Registry
                (http://www.faa.gov/licenses_certificates/aircraft_certification/aircraft_registry/releasable_aircraft_download/)
  airports      Store / import data from the FADDS "APT" database - includes airport facilities, runways, attendance
                hours and remarks specific to those three items.
  awoses        Store / import data from the FADDS "AWOS" database - this lists all "automated weather observation
                stations" with their locations, codes, and phone numbers.
  fixes         Store / import data from the FADDS "FIX" database - this includes locations of all fixes published in
                the national airspace system.

As an extra bonus, the import-airspace-shapes.sh script will populate a database with geometry for US restricted
airspace. It doesn't use Django. Sources are the shapefiles in FADDS and the SoaringWeb OpenAir files at
http://soaringweb.org/Airspace/NA/HomePage.html


Detailed usage notes:

Postgres:

Create a clean database named "faadata"
Do the postgis spatial stuff to add functions, CRS, etc. See
https://docs.djangoproject.com/en/dev/ref/contrib/gis/install/#spatialdb-template


Django setup:

Get faadata and faddsdata from github
Put those two python libraries in your PYTHONPATH
Add the apps you desire to settings.INSTALLED_APPS
python manage.py migrate
python manage.py runserver
test the server
  http://127.0.0.1:8000/airports/ should be empty
  http://127.0.0.1:8000/airports/SQL/ should return a 404 saying "No airport found matching the query"

Data import:

Download and unpack the FADDS zip
Disable DEBUG in settings.py

Loading it all (excluding aircraft, which is a different dataset and path):

  Add faadata.fadds, faadata.airports, faadata.awoses, faadata.fixes to INSTALLED_APPS
  python manage.py fadds_import --faddspath=$HOME/src/faa-postgis/Oct20-Dec15/
  This takes a few minutes

Loading specific datasets:
  Add faadata.aircraft to INSTALLED_APPS
  manage.py aircraft_import --path=/path/to/AR-folder/ will then import all the aircraft registrations

  Add faadata.airports to INSTALLED_APPS
  manage.py airport_import --path=/path/to/fadds/ will import all airports, runways, remarks, and attendance schedules. There is not-yet exposed granularity in the import to select which of those you want imported in the management command itself.

  Add faadata.awoses to INSTALLED_APPS
  manage.py awos_import --path=/path/to/fadds/ will import all automated weather observation stations

  Add faadata.fixes to INSTALLED_APPS
  manage.py fix_import --path=/path/to/fadds/ will import all fixes (note: a "fix" is a location used by pilots flying under Instrument Flight Rules. It is not a "physical" place just a set of pronounceable characters mapping to a latitude/longitude.)

Re-enable DEBUG in settings.py (if desired)

Check your work:
`python manage.py runserver`
test the server
  http://127.0.0.1:8000/airports/ should show page 1 of 996 or so with 20 airports
  http://127.0.0.1:8000/airports/SQL/ should show data for San Carlos
