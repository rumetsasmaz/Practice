import socket

def scan_port_range(start_port , end_port):
    target_ip = "127.0.0.1"
   
    print(f"[+] Scanning {target_ip} from port {start_port} to {end_port}...")

    for port in range(start_port , end_port + 1 ):
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((target_ip , port))

        if result == 0:
            print(f"[SUCCESS] Port {port}: OPEN")
        else:
            print(f"[FAILED] Port {port} CLOSED") 

        s.close()


try:
    start = int(input("Enter A Start Port: "))
    end = int(input("Enter A End Port: "))
    scan_port_range(start , end)       
except ValueError:
    print("[-] Error: Please enter a valid port number!")