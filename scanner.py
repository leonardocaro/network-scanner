import socket

host = "127.0.0.1"

print(f"Scanning {host}...")

# local HTTP server is running on port 8000
for port in range(7995, 8006):
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    result = sock.connect_ex((host, port))

    if result == 0:
        print(f"[+] Port {port} is OPEN")

    sock.close()

print("Scan complete.")
