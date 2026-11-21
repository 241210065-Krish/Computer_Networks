import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.sendto(b"Hello from client!", ('localhost', 12345))
data, addr = client_socket.recvfrom(1024)
print("Received:", data.decode())
client_socket.close()