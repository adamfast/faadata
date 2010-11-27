This project provides Django models and simple import scripts to load data provided by the Federal Aviation Administration.

Sub-apps:
  aircraft      Store / import data from the public Aircraft Registry (http://www.faa.gov/licenses_certificates/aircraft_certification/aircraft_registry/releasable_aircraft_download/)
  airports      Store / import data from the FADDS "APT" database - includes airport facilities, runways, attendance hours and remarks specific to those three items. This app is in a "pre-beta" state, the parsers are there to break everything apart but no models exist to store the data and the import process isn't done yet, either.

Installation:
  Add faadata.aircraft to INSTALLED_APPS
  Set settings.FAA_AIRCRAFT_DB_PATH to the path to the registry file downloaded from the above link
  export your DJANGO_SETTINGS_MODULE
  python aircraft/load.py will then import all the aircraft registrations
