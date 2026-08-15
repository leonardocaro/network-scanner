import argparse
import socket


def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    result = sock.connect_ex((host, port))

    sock.close()

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