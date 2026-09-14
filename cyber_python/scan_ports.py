import socket
def scan_ports(port_list):

    target_ip = "127.0.0.1"

    print(f"[+] Started port scan at...\n{target_ip} ")

    for port in port_list: # type: ignore
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((target_ip, port))

        if result == 0:
            print(f"[SUCCESS] Port {port}: OPEN")
        else:
            print(f"[FAILED] Port {port}: CLOSED")


        s.close()

ports = [21, 22, 80, 135, 443, 445]

scan_ports(ports)

print(f"\n[+] Scan Completed")
