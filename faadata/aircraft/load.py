import datetime
import sys
from django import db
from django.conf import settings
from faadata.aircraft.models import AircraftRegistration, AircraftManufacturerCode
from faadata.aircraft.parser import AircraftRegistration as AircraftRegistrationParser
from faadata.aircraft.parser import AircraftManufacturerCode as AircraftManufacturerCodeParser

# for the file I have, the line count is 369,952 total.
# One blank line at the end, and the header line. That means I should get a final count of 369,952 total.
NUMBER_OF_LINES_SPOTTED_IN_FILE = 369952

def import_aircraftmanufacturercodes(path):
    raw = open(path + 'ACFTREF.txt')

    for line in raw:
        if len(line) > 10: # basically just to catch the last line with its single char
            if line[:4] == 'CODE':
                pass
            else:
                data = AircraftManufacturerCodeParser(line)
                record = AircraftManufacturerCode.objects.get_or_create(code=data.code)[0]
                record.manufacturer = data.manufacturer
                record.model = data.model
                record.aircraft_type = data.aircraft_type
                record.engine_type = data.engine_type
                record.category = data.category
                record.builder_certification_code = data.builder_certification_code
                record.number_of_engines = data.number_of_engines
                record.number_of_seats = data.number_of_seats
                record.aircraft_weight = data.aircraft_weight
                record.cruising_speed = data.cruising_speed
                record.save()


def import_aircraftregistration(path):
    raw = open(path + 'MASTER.txt')

    count = 0
    for line in raw:
        if len(line) > 10: # basically just to catch the last line with it's single char
            if line[3:11] == 'N-NUMBER':
                pass
            else:
                try:
                    data = AircraftRegistrationParser(line)
                    record = AircraftRegistration.objects.get_or_create(n_number=data.n_number)[0]
                    record.serial_number = data.serial_number
                    record.aircraft_mfr_model_code = data.aircraft_mfr_model_code
                    record.engine_mfr_model_code = data.engine_mfr_model_code
                    record.year_mfg = data.year_mfg
                    record.type_registrant = data.type_registrant
                    record.registrant_name = data.registrant_name
                    record.street1 = data.street1
                    record.street2 = data.street2
                    record.city = data.city
                    record.state = data.state
                    record.zip_code = data.zip_code
                    record.region = data.region
                    record.county = data.county
                    record.country = data.country
                    record.last_activity_date = data.last_activity_date
                    record.certificate_issue_date = data.certificate_issue_date
                    record.airworthiness_classification_code = data.airworthiness_classification_code
                    record.aircraft_type = data.aircraft_type
                    record.engine_type = data.engine_type
                    record.status_code = data.status_code
                    record.mode_s_code = data.mode_s_code
                    record.fractional_ownership = data.fractional_ownership
                    record.airworthiness_date = data.airworthiness_date
                    record.other_name_1 = data.other_name_1
                    record.other_name_2 = data.other_name_2
                    record.other_name_3 = data.other_name_3
                    record.other_name_4 = data.other_name_4
                    record.other_name_5 = data.other_name_5
                    record.expiration_date = data.expiration_date
                    record.save()
                except KeyboardInterrupt:
                    exit()
                except:
                    print line
                    print sys.exc_info()[0]
                    print sys.exc_info()[1]

                count = count + 1
                if count % 100 == 0: # every hundred
                    db.reset_queries() # clear the "cache" of SQL queries every hundred to keep it from absolutely killing memory

        else: # line shorter than 10
            print ('Line less than 10. *%s*' % line)

    print('Imported count was %s' % count)
    print('Last manually updated (expected) count was %s' % NUMBER_OF_LINES_SPOTTED_IN_FILE)
    print('A difference of %s' % (int(NUMBER_OF_LINES_SPOTTED_IN_FILE) - int(count)))

if __name__ == '__main__':
    # You can get the FAA Aircraft database from: http://www.faa.gov/licenses_certificates/aircraft_certification/aircraft_registry/releasable_aircraft_download/
    if getattr(settings, 'FAA_AIRCRAFT_DB_PATH', False):
        start_time = datetime.datetime.now()
        import_aircraftregistration(settings.FAA_AIRCRAFT_DB_PATH)
        import_aircraftmanufacturercodes(settings.FAA_AIRCRAFT_DB_PATH)
        print('Took %s' % (datetime.datetime.now() - start_time))
#        print('Assuming manual count (%s) that is %s sec. per record' % (int(NUMBER_OF_LINES_SPOTTED_IN_FILE), (datetime.datetime.now() - start_time) / int(NUMBER_OF_LINES_SPOTTED_IN_FILE)))
    else:
        print('Do not know path to find the file. Set FAA_AIRCRAFT_DB_PATH.')
