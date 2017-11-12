from configparser import ConfigParser
from contact_storage import CSVContactStorage, JSONContactStorage
from controller import OperationController, TelnetController


def get_init_config():
    parser = ConfigParser()
    parser.read('config.ini')
    return parser['DEFAULT']['format'].lower()

file_format = get_init_config()
if file_format == 'json':
    storage = JSONContactStorage()
elif file_format == 'csv':
    storage = CSVContactStorage()
else:
    raise Exception('Unknown format inserted into init.py')


if __name__ == '__main__':
    while True:
        try:
            storage.read()
            controller = TelnetController(operation_name.strip())
            if controller.operation_name == 'X':
                break
            if controller.operation_name in ['R', 'C']:
                cl_socket.sendall(str(result).encode('utf8'))
            storage.write()
        except Exception as e:
            print(e.__str__())
            storage.write()
            continue
    server_socket.close()
    cl_socket.close()
