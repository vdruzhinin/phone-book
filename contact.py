import json

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __eq__(self, other):
        return self.name == other.name and \
               self.phone == other.phone

    def toJSON(self):
        return json.dumps({self.name: self.phone})
