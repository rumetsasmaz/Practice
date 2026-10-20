import socket

class BaseModule:

    def __init__(self , target, timeout=1):
        self.target = target
        self.timeout = timeout

    def run(self):

        raise NotImplementedError()

class PortScannerModule(BaseModule):

    def __init__(self, target , *ports , timeout=1):
        self.ports = ports
        for port in ports:
            if not(1 <= port <= 65535):
                raise ValueError(f"Invalid Port: {port}")   

        super().__init__(target, timeout)
    
    def check_port(self, port):

        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        s.settimeout(self.timeout)
        try:
            s.connect((self.target, port))
            
        except (ConnectionRefusedError, TimeoutError):
            return False
        else:
            return True
        finally:
            s.close()
    
    def run(self):
        print(f"[*] Starting Port Scan: {self.ports}")

        for port in self.ports:
            if self.check_port(port):
                print(f"[+] {port} OPEN")
            else:
                print(f"[-] {port} CLOSED")

class ReverseDNSModule(BaseModule):

    def __init__(self, *ips , timeout=2):
        self.ips = ips
        super().__init__("multiple IP's", timeout)

    def lookup(self, ip):

        try:
            result = socket.gethostbyaddr(ip)
        except (socket.herror , socket.gaierror):
            return None
        else:
            return result[0]

    def run(self):

        for ip in self.ips:
            result = self.lookup(ip)
            if result is None:
                print(f"[-] {ip} -> No Record")
            else:
                print(f"[+] {ip} -> {result}")


if __name__ == "__main__":

    my_ports = [22, 80, 135, 445]
    modules = [

            PortScannerModule("127.0.0.1", *my_ports, timeout=2),
            ReverseDNSModule("8.8.8.8", "1.1.1.1"),
            ]
    for module in modules:
        module.run()
        print("-" * 40)

    try:
        PortScannerModule("127.0.0.1", 80 , 99999999)

    except ValueError as e:
        print(e)