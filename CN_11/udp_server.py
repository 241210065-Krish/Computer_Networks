import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))
print("UDP Server is ready...")

data, addr = server_socket.recvfrom(1024)
print("Received:", data.decode())
server_socket.sendto(b"Hello from server!", addr)
server_socket.close()