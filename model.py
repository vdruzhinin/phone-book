class ContactOperations:

    @staticmethod
    def add_contact(contact_storage, contact):
        contact_storage.append(contact)
        return contact

    @staticmethod
    def get_contact_list(contact_storage):
        return contact_storage.get_contacts()

    @staticmethod
    def remove_contact(contact_storage, contact):
        if contact_storage.contain_name(contact.name):
            contact_storage.delete_contact_by_name(contact.name)
        else:
            raise Exception('Given name not exist in contact storage')

    @staticmethod
    def update_contact(contact_storage, contact):
        if contact_storage.contain_name(contact.name):
            in_cont = contact_storage.get_contact_by_name(contact.name)
            in_cont = contact
        else:
            contact_storage.add(contact)
