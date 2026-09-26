import socket

class PortScanner:
    def __init__(self , target_ip):
        self.target_ip = target_ip
        self.open_ports = []

    def check_ports(self , port):
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((self.target_ip , port))
        s.close()

        if result == 0:
            self.open_ports.append(port)
            return True 
        else:
            return False

    def scan_range(self , start_port , end_port):

        for port in range(start_port , end_port + 1):
   
            if self.check_ports(port) == True:

                print(f"[+] Port {port} Is OPEN")
            else:
                print(f"[-] Port {port} Is CLOSED")


    def save_results(self, filename="scan_results.txt"):
        with open(filename, "w") as file:  
            file.write(f"Target IP: {self.target_ip}\n")
            file.write(f"Open Ports: {self.open_ports}\n")

scanner_local = PortScanner("127.0.0.1")
scanner_local.scan_range(130 , 135)
scanner_local.save_results()


scanner_router = PortScanner("192.168.1.1")
scanner_router.scan_range(10 , 60)
scanner_router.save_results("router_results.txt")


print("\n--- SUMMARY ---")
print(f"Local Open Ports: {scanner_local.open_ports}")
print(f"Router Open Ports: {scanner_router.open_ports}")