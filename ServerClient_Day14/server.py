import socket
import time
import pickle

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    # now our endpoint knows about the other endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from (address) has been established. ")

    d = {1: "hi", 2: "there"}
    msg = pickle.dumps(d)
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8') + msg
    print(msg)
    clientsocket.send(msg)
    """
    while True:
        time.sleep(3)
        msg = f"The time is {time.time()}"
        msg = f"{len(msg):<{HEADERSIZE}}" + msg

        print(msg)
        clientsocket.send(bytes(msg, "utf-8"))
    """
