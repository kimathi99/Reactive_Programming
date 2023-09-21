import socket
import random
import time
import threading

# Function to handle a client's connection
def handle_client(client_socket, client_address):
    print(f"Connected to client at {client_address}")

    while True:
        # Send the shared random number to the client
        client_socket.sendall(str(shared_random).encode())

        # Wait for 30 milliseconds before generating the next number
        time.sleep(1)

# Function to update the shared random number every 0.9 seconds
def update_shared_random():
    global shared_random
    while not exit_signal.is_set():  # Continue updating unless exit_signal is set
        shared_random = round(random.uniform(0, 100), 2)
        time.sleep(0.9)  # Update every 0.9 seconds

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific host and port
host = '127.0.0.1'  # localhost
port = 12345  # You can choose any available port

server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(10)  # Allow up to 10 simultaneous connections
print(f"Server is listening on {host}:{port}")

# Initialize the shared random number
shared_random = round(random.uniform(0, 100), 2)

# Create an event to signal server exit
exit_signal = threading.Event()

try:
    # Start a thread to update the shared random number
    update_thread = threading.Thread(target=update_shared_random)
    update_thread.start()

    while not exit_signal.is_set():
        # Accept a connection from a client
        client_socket, client_address = server_socket.accept()

        # Start a new thread to handle the client with the shared random number
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

    # Wait for all client threads to finish
    client_handler.join()

except KeyboardInterrupt:
    # Set the exit signal when 'q' is pressed
    exit_signal.set()

    # Wait for the update thread to finish
    update_thread.join()

    print("Server has been terminated.")
