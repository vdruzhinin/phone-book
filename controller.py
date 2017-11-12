from model import ContactOperations
import socket


class OperationController:
    operation_list = {
        'C': ContactOperations.add_contact, 'R': ContactOperations.get_contact_list,
        'U': ContactOperations.update_contact, 'D': ContactOperations.remove_contact
    }

    def execute(self, operation_name):
        try:
            self.execute_operation = OperationController.operation_list[operation_name]
        except Exception:
            raise Exception('Wrong operation. Please correct.')

    def send(self):
        pass

    def receive(self):
        pass


class TelnetController(OperationController):

    def __init__(self):
        self.s = socket.socket()
        self.s.bind(('127.0.0.1', 5001))
        self.s.listen(5)
        self.c, a = self.s.accept()
        super(TelnetController, self).__init__()

    def send(self):
        self.c.sendall(b'Please choose operation:\n'
                       b'\tC - create contact\n'
                       b'\tR - show contacts\n'
                       b'\tU - update exist contact by name\n'
                       b'\tD - remove contact by name\n'
                       b'\tX - Exit from program\n')

    def receive(self):
        self.operation_name = self.c.recv(1024).decode().strip()

    def close(self):
        self.c.close()
        self.s.close()