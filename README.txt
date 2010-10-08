This project provides Django models and simple import scripts to load data provided by the Federal Aviation Administration.

Sub-apps:
  aircraft    Store / import data from the public Aircraft Registry (http://www.faa.gov/licenses_certificates/aircraft_certification/aircraft_registry/releasable_aircraft_download/)


Installation:
  Add faadata.aircraft to INSTALLED_APPS
  Set settings.FAA_AIRCRAFT_DB_PATH to the path to the registry file downloaded from the above link
  export your DJANGO_SETTINGS_MODULE
  python aircraft/load.py will then import all the aircraft registrations
