import argparse
import socket


<<<<<<< HEAD
def scan_port(host, port):
=======
print(f"Scanning {host}...")

# local HTTP server is running on port 8000
for port in range(7995, 8006):
    
>>>>>>> 4015d4a37c038bf6cc5527c4cc856c995434d6a0
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    result = sock.connect_ex((host, port))

    sock.close()

<<<<<<< HEAD
    return result == 0


def main():
    parser = argparse.ArgumentParser(
        description="Simple TCP port scanner"
    )

    parser.add_argument(
        "host",
        help="IP address or hostname to scan"
    )

    args = parser.parse_args()

    host = args.host

    print(f"Scanning {host}...")

    for port in range(1, 10001):

        if scan_port(host, port):
            print(f"[+] Port {port} is OPEN")

    print("Scan complete.")


if __name__ == "__main__":
    main()
=======
print("Scan complete.")
>>>>>>> 4015d4a37c038bf6cc5527c4cc856c995434d6a0
