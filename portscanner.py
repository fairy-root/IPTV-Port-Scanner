from queue import Queue
import socket
import threading
import logging
from colorama import Fore

target = input(Fore.GREEN + "Input the target IP Address: ")
queue = Queue()
open_ports = []
op = int(input(Fore.GREEN + "Choose a Mode\n\nMode 1: Range [1 - 1024]\nMode 2: Range [1 - 49152]\nMode 3: Known Ports [80, 8000, 8080, 433...]\nMode 4: Enter a specific Port\n\nEnter only the number: "))
if not isinstance(op, int):
    try:
        op = int(op)
    except ValueError:
        print("The value entered is not an integer.")

logger = logging.getLogger(__name__)

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except Exception as e:
        #logger.exception("An error occurred while scanning port %d: %s", port, e)
        return False
    finally:
        sock.close()

def get_ports(mode, specific_port=None):
    if mode not in [1, 2, 3, 4]:
        print("Error: Please enter a valid mode (1, 2, 3, or 4)")
        return
    if mode == 1:
        print("You have choosen Mode 1: Range [1 - 1024]\n")
        for port in range(1, 1024):
            queue.put(port)
    elif mode == 2:
        print("You have choosen Mode 2: Range [1 - 49152]\n")
        for port in range(1, 49152):
            queue.put(port)
    elif mode == 3:
        print("You have choosen Mode 3: Known Ports [80, 8000, 8080, 433...]\n")
        ports = [433, 57050, 25461, 6464, 7571, 8000, 16004, 999, 2052, 8080, 1234, 88, 4554, 2023, 82, 1991, 8555, 36936, 8880, 11026, 1026, 15001, 25463, 8789, 4646, 1997, 9966, 28506, 83, 18800, 2082, 826, 85, 7444, 13500, 2086, 7477, 8800, 15000, 30003, 2095, 24000, 1979, 89, 81, 2083, 1453, 36995, 5115, 7040, 2017, 7646, 2080, 8081, 7000, 41000, 8666, 43100, 1801, 8085, 34567, 1925, 16161, 1557, 5000, 2103, 443, 1339, 12974, 8011, 8001, 9898, 12000, 7575, 48555, 1962, 2999, 2021, 777, 9000, 12060, 31000, 37500, 19553, 80, 2016, 1978, 1985, 3800, 8691, 6092, 25510, 3500, 9600, 8883, 8088, 1983, 7879, 8899, 8089, 5500, 8888, 7200, 8898, 9999, 5487, 22461, 2112, 8037, 9300, 5050, 35461, 1935, 6212, 17898, 6767, 7070, 8060, 3334, 8484, 33612, 23000, 6969, 7788, 21000, 15800, 2020, 5909, 1558, 8008, 8181, 8787, 11118, 1223, 5475, 5436, 8091, 16000, 6453, 9198, 27000, 57999, 3456, 50750, 2540, 8844, 888, 25462, 90, 1122, 8090, 59000, 2089, 2578, 1155, 8118, 8999, 24561, 1194, 8443, 9181, 1551]
        for port in ports:
            queue.put(port)
    elif mode == 4:
        ports = input("Enter your Port/Ports - seperate by blank: ")
        print("You have choosen Mode 4: Scanning the ports...\n")
        try:
            ports = ports.split()
            ports = list(map(int, ports))
            for port in ports:
                queue.put(port)
        except ValueError:
            print("Error: Please enter a valid port number (integer)")

def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open!".format(port))
            open_ports.append(port)

def run_scanner(threads, mode):

    get_ports(mode)

    thread_list = []

    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    print("Open ports are:", open_ports)
    for i in open_ports:
        print(f"bleedout -h {target} -p {i} -t 50")

run_scanner(100, op)