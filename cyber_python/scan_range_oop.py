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

    def save_results(self , filename="scan_results.txt"):
        with open("scan_results.txt" , "w") as file:
            file.write(f"Target IP: {self.target_ip}\n")
            file.write(f"Open Ports: {self.open_ports}\n")      


scanner = PortScanner("127.0.0.1")
scanner.scan_range(130 , 140)
scanner.save_results()

print("\n--- SUMMARY ---")
print(f"Found Open Ports: {scanner.open_ports}")