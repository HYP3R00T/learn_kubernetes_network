import socket
import time
import random
import os
import sys

# Configuration via environment variables
HOST = os.getenv("SERVER_HOST", "0.0.0.0")  # Default to all network interfaces
PORT = int(os.getenv("SERVER_PORT", 5000))  # Default port 5000


def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server_socket.bind((HOST, PORT))
    except OSError as e:
        if e.errno == 98:  # Address already in use
            print(f"Error: Port {PORT} is already in use.")
            sys.exit(1)
        else:
            print(f"Error binding server: {e}")
            sys.exit(1)

    server_socket.listen(1)
    print(f"Server listening on {HOST}:{PORT}")

    try:
        while True:
            conn, addr = server_socket.accept()
            print(f"Connection established with {addr}")
            with conn:
                while True:
                    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                    random_number = random.randint(1, 100)
                    message = f"{random_number} @ {timestamp}\n"
                    try:
                        conn.sendall(message.encode("utf-8"))
                        print(f"Sent: {message}", end="")
                        time.sleep(1)
                    except BrokenPipeError:
                        print("Client disconnected")
                        break
    except KeyboardInterrupt:
        print("\nServer is shutting down gracefully...")
    finally:
        # Explicitly close the socket when done
        server_socket.close()
        print("Socket closed, port released.")


if __name__ == "__main__":
    run_server()
