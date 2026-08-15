import argparse
import socket


def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    result = sock.connect_ex((host, port))

    sock.close()

    return result == 0

def parse_port_range(port_range):
    start, end = port_range.split("-")

    return int(start), int(end)


def main():
    parser = argparse.ArgumentParser(
        description="Simple TCP port scanner"
    )

    parser.add_argument(
        "host",
        help="IP address or hostname to scan"
    )

    parser.add_argument(
        "--ports",
        default="1-1024",
        help="Port range to scan (default: 1-1024)"
    )

    args = parser.parse_args()

    host = args.host

    start_port, end_port = parse_port_range(args.ports)

    print(f"Scanning {host}...")

    for port in range(start_port, end_port + 1):

        if scan_port(host, port):
            print(f"[+] Port {port} is OPEN")

    print("Scan complete.")


if __name__ == "__main__":
    main()
