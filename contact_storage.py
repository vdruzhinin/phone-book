import json
import csv
from contact import Contact


class BaseStorage:

    def __init__(self, data):
        self.data = data

    def read(self):
        pass

    def write(self):
        pass

    def contain_name(self, contact):
        return bool(self.get_contact_by_name(contact.name))

    def get_contact_by_name(self, name):
        result = list(filter(lambda x: x.name == name, self.data))
        return result[0] if result else None

    def delete_contact_by_name(self, name):
        self.data = list(filter(lambda x: x.name != name, self.data))

    def add(self, contact):
        self.data.append(contact)

    def get_contacts(self):
        return self.data


class JSONContactStorage(BaseStorage):

    def __init__(self, data=[]):
        super().__init__(data)

    def read(self):
            with open('phones.json', 'r+') as file:
                loaded_json = json.load(file)
                for item in loaded_json:
                    for name, phone in item.items():
                        self.data.append(Contact(name, phone))

    def write(self):
        with open('phones.json', 'w') as file:
            json.dump(self.data, file, indent=4)


class CSVContactStorage(BaseStorage):

    def __init__(self, data=[]):
        super().__init__(data)

    def read(self):
        with open('phones.csv', 'r+') as file:
            contact_dictionary = csv.DictReader(file, delimiter=',', quotechar='"')
            for contact in contact_dictionary:
                self.data = Contact(contact['name'], contact['phone'])

    def write(self):
        with open('phones.csv', 'w') as file:
            writer = csv.DictWriter(
                file, fieldnames=['name', 'phone'], delimiter=',', quotechar='"'
            )
            writer.writeheader()
            for contact in self.data:
                writer.writerow(
                    {
                        'name': contact.name,
                        'phone': contact.phone
                    }
                )
