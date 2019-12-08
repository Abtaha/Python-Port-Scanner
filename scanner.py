import socket

# Takes address as input
addr = input("Enter IP address >>> ")


# Loops over all the ports
for port in range(65535 + 1):
    # Creates socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, )
    
    # Connects to socket
    result = sock.connect_ex((addr, port))
    if result == 0:
        print("Port ", port, " is open")
        sock.close()