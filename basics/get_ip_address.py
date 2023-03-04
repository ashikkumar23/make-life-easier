"""
The `socket` library in Python can be used to get the IP address of the local machine using the `gethostname()` and `gethostbyname()` functions.
The `gethostname()` function returns the hostname of the current machine, and `gethostbyname()` returns the IP address corresponding to the hostname.

To retrieve public ip address, we can use third-party services like https://api.ipify.org/ or https://ipinfo.io/ip
"""

import socket

import requests


def get_local_ip_address() -> str:
    """Returns the local IP address of the current machine."""
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)


def get_public_ip_address() -> str:
    """Returns the public IP address of the current machine."""
    response = requests.get("https://api.ipify.org")  # Or use, https://ipinfo.io/ip
    return response.text.strip()


if __name__ == "__main__":
    local_ip_address = get_local_ip_address()
    print(f"Local IP Address: {local_ip_address}")
    public_ip_address = get_public_ip_address()
    print(f"Public IP Address: {public_ip_address}")
