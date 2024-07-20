import socket
import subprocess
import sys
import os

def clear_screen():
    """Clear the terminal screen based on the operating system."""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix-based systems (Linux, macOS)
        os.system('clear')

# Clear the screen
clear_screen()

# Ask for input
remoteServer = input("Enter a remote host to scan: ")
try:
    remoteServerIP = socket.gethostbyname(remoteServer)
except socket.gaierror:
    print('Hostname could not be resolved. Exiting.')
    sys.exit()

# Print a nice banner with information on which host we are about to scan
print("-" * 60)
print(f"Please wait, scanning remote host {remoteServerIP}")
print("-" * 60)

# Using the range function to specify ports (here it will scan all ports between 1 and 1024)
# We also put in some error handling for catching errors

try:
    for port in range(1, 1025):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # Optional: Set timeout to avoid long waits
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print(f"Port {port}: Open")
except KeyboardInterrupt:
    print("\nYou pressed Ctrl+C. Exiting.")
    sys.exit()
except socket.error:
    print("Couldn't connect to server. Exiting.")
    sys.exit()
