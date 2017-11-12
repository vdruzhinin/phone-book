import sqlite3
from contact import Contact


class SQLLiteOperations:

    _connection = sqlite3.connect('db.sqlite3')
    _cursor = _connection.cursor()
    _db_name = 'phones'
    _select_all = _cursor.execute("SELECT * FROM {}".format(_db_name))

    @staticmethod
    def get_contact_list():
        return [Contact(cont[1], cont[2]) for cont in SQLLiteOperations._select_all]

    # @staticmethod
    # def remove_contact(contact):
    #     if contact_storage.contain_name(contact.name):
    #         contact_storage.delete_contact_by_name(contact.name)
    #     else:
    #         raise Exception('Given name not exist in contact storage')

print(SQLLiteOperations.get_contact_list()[0].phone)