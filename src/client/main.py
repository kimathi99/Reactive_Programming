import socket

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server host and port
host = '127.0.0.1'  # localhost
port = 12345  # Make sure it matches the server's port

# Connect to the server
client_socket.connect((host, port))
print(f"Connected to server at {host}:{port}")

try:
    while True:
        # Receive the random number from the server
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"Received random number: {data}")
except KeyboardInterrupt:
    pass

# Close the client socket
client_socket.close()
