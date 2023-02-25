"""
The `socket` library in Python can be used to get the IP address of the local machine using the `gethostname()` and `gethostbyname()` functions.

The `gethostname()` function returns the hostname of the current machine, and `gethostbyname()` returns the IP address corresponding to the hostname.
"""

import socket


def get_local_ip_address() -> str:
    """Returns the local IP address of the current machine."""
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address


if __name__ == "__main__":
    local_ip_address = get_local_ip_address()
    print(f"Local IP Address: {local_ip_address}")
