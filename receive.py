import socket
import struct
import sys

def get_ip():
    if socket.gethostbyname(socket.getfqdn()) == "127.0.0.1":
        ip = input("enter your ip address: ")
        address = (ip, 8888)
    else:
        ip = socket.gethostbyname(socket.getfqdn())
        address = (ip, 8888)
    return address

address = get_ip()

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except (socket.error, msg):
    print("failed to create socket.error code: " + str(msg[0]) + ", error message: " + msg[1])

#sys.exit()
print()
print_address = " * Socket Created at http://" + str(address[0]) + ":" + str(address[1]) + "/ (Press CTRL+C to quit)"
print(print_address)
s.bind(address)
s.listen(5)

while True:
    (client, addr) = s.accept()
    print("got connected from", client, addr)
    buf = b""
    while len(buf)<4:
        buf += client.recv(4-len(buf))
    size = struct.unpack("!i", buf)
    print("receiving %s bytes" % size)

    with open("tst.jpg", "wb") as img:
        while True:
            data = client.recv(1024)
            print(data)
            if not data:
                break
            img.write(data)
    img.close()
print("received!!")
client.close()