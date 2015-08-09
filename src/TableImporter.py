import utils
import ConfigParser


class TableImporter(object):

    def __init__(self, settings):
        self.config = ConfigParser.SafeConfigParser()
        self.config.read(settings)

    def create_table(self):
        raise NotImplementedError()

    def populate_table(self):
        raise NotImplementedError()

    def __del__(self):
        raise NotImplementedError()


def import_table(table_class_name, settings):
    ti = utils.str_to_object(table_class_name, table_class_name, settings)
    ti.create_table()
    ti.populate_table()
