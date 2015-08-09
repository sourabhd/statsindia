from __future__ import print_function
import TableImporter
import sys
import gc


class PlacesTableImporter(TableImporter.TableImporter):
    """ Imports metadata related to places"""

    def __init__(self, settings):
        super(PlacesTableImporter, self).__init__(settings)
        self.db_type = self.config.get('db', 'db_type')
        self.db_folder = self.config.get('db', 'db_folder')
        self.db_file = self.config.get('db', 'db_file')
        self.web2py_loc = self.config.get('db', 'web2py_loc')
        print(self.db_type)
        print(self.db_folder)
        print(self.db_file)
        print(self.web2py_loc)
        # Add DAL to path
        sys.path.append(self.web2py_loc)
        # import required objects
        from gluon.dal import DAL
        # establish a database connection
        self.db = DAL(self.db_type + '://' + self.db_file,
                      folder=self.db_folder)

    def create_table(self):
        from gluon.dal import Field
        self.db.define_table('places',
                             Field('placeID', 'integer'),
                             Field('countryID', 'integer', default=0),
                             Field('stateID', 'integer', default=0),
                             Field('districtID', 'integer', default=0),
                             Field('localityID', 'integer', default=0),
                             Field('name', 'string'))

    def populate_table(self):
        print(self.db.places.insert(placeID=1, countryID=1, stateID=2,
                                    districtID=3, localityID=4,
                                    name='Pune'))
        print(self.db.places.insert(placeID=2, countryID=11, stateID=12,
                                    districtID=3, localityID=4,
                                    name='Hyderabad'))
        print(self.db.places.insert(placeID=3, countryID=21, stateID=42,
                                    districtID=53, localityID=64,
                                    name='Mumbai'))
        print(self.db.places.insert(placeID=4, countryID=1, stateID=22,
                                    districtID=23, localityID=41,
                                    name='Junagad'))
        print(self.db.places.insert(placeID=5, countryID=111, stateID=2,
                                    districtID=3, localityID=49,
                                    name='Lohagad'))
        print(self.db.places.insert(placeID=6, countryID=18, stateID=42,
                                    districtID=13, localityID=4,
                                    name='Raipur'))
        print(self.db.places.insert(placeID=7, countryID=14, stateID=24,
                                    districtID=3, localityID=444,
                                    name='Rampur'))
        print(self.db.places.insert(placeID=8, countryID=1, stateID=2,
                                    districtID=3,
                                    name='Nagpur'))
        print(self.db.places.insert(placeID=9, countryID=1, stateID=2,
                                    name='Maharashtra'))
        print(self.db.places.insert(placeID=10, countryID=1,
                                    name='India'))

    def __del__(self):
        if self.db:
            self.db.commit()
            self.db.close()
            self.db = None
            gc.collect()
