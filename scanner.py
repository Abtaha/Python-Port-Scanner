import socket

addr = input("Enter IP address >>> ")

for port in range(0, 65535):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, )
    
    result = sock.connect_ex((addr, port))
    if result == 0:
        print("Port ", port, " is open")
        sock.close()