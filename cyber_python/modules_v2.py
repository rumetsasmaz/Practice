import socket

class BaseModule:

    def __init__(self , target, timeout=1):
        self.target = target
        self.timeout = timeout

    def run(self):

        raise NotImplementedError()\

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



if __name__ == "__main__":

    BaseModule("x").run()