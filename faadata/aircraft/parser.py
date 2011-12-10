import datetime

class AircraftManufacturerCode(object):
    def __init__(self, record):
        self.code = record[:7].strip()
        self.manufacturer = record[8:38].strip()
        self.model = record[39:59].strip()
        self.aircraft_type = record[60].strip()
        self.engine_type = record[62].strip()
        self.category = record[64].strip()
        self.builder_certification_code = record[66].strip()
        self.number_of_engines = record[68:70].strip()
        self.number_of_seats = record[71:74].strip()
        self.aircraft_weight = record[75:82].strip()
        self.cruising_speed = record[83:87].strip()

class AircraftRegistration(object):
    def __init__(self, record):
        # first parse the fixed-width
        self.n_number = record[:5].strip()
        self.serial_number = record[6:36].strip()
        self.aircraft_mfr_model_code = record[37:44].strip()
        self.engine_mfr_model_code = record[45:50].strip()
        self.year_mfg = record[51:55].strip()
        if record[56].strip():
            self.type_registrant = record[56].strip()
        else:
            self.type_registrant = None
        self.registrant_name = record[58:108].strip()
        self.street1 = record[109:142].strip()
        self.street2 = record[143:176].strip()
        self.city = record[177:195].strip()
        self.state = record[196:198].strip()
        self.zip_code = record[199:209].strip()
        self.region = record[210].strip()
        self.county = record[212:215].strip()
        self.country = record[216:218].strip()
        if record[219:227].strip():
            self.last_activity_date = datetime.datetime.strptime(record[219:227], "%Y%m%d").date()
        else:
            self.last_activity_date = None
        if record[228:236].strip():
            self.certificate_issue_date = datetime.datetime.strptime(record[228:236], "%Y%m%d").date()
        else:
            self.certificate_issue_date = None
        self.airworthiness_classification_code = record[237:238].strip()
        if record[248].strip():
            self.aircraft_type = record[248].strip()
        else:
            self.aircraft_type = None
        if record[250:252].strip():
            self.engine_type = record[250:252].strip()
        else:
            self.engine_type = None
        self.status_code = record[253:255].strip()
        self.mode_s_code = record[256:264].strip()
        self.fractional_ownership = record[265].strip()
        if record[267:275].strip():
            self.airworthiness_date = datetime.datetime.strptime(record[267:275], "%Y%m%d").date()
        else:
            self.airworthiness_date = None
        self.other_name_1 = record[276:326].strip()
        self.other_name_2 = record[327:377].strip()
        self.other_name_3 = record[378:428].strip()
        self.other_name_4 = record[429:479].strip()
        self.other_name_5 = record[480:530].strip()
        if record[531:539].strip():
            self.expiration_date = datetime.datetime.strptime(record[531:539], "%Y%m%d").date()
        else:
            self.expiration_date = None
