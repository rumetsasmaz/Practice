import socket

class BaseModule:
    def __init__(self , target):
        self.target = target

    def run(self):

        raise NotImplementedError()

class PortScannerModule(BaseModule):

    def __init__(self , target , ports):

        for port in ports:
            if port < 1 or port > 65535:
                raise ValueError(f"Invalid Port: {port}")

        super().__init__(target)
        self.ports = ports

    def run(self):
        print(f"[*] Starting Port Scan: {self.target}")

        for port in self.ports:
            s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((self.target , port))
            s.close()
            if result == 0:
                print(f"[+] Port {port}: OPEN")
            else:
                print(f"[-] Port {port}: CLOSED")

class SubDomainModule(BaseModule):
    def __init__(self  , target , wordlist):
        super().__init__(target)
        self.wordlist = wordlist

    def run(self):
        print(f"[*] Starting SubDomain Scan: {self.target}")
        try:
            for sub in self.wordlist:
                print(f"[+] Domain founded: {sub}.{self.target}")
        except Exception as e:
            print(f"[-] Error during subdomain scanning: {e}")


if __name__ == "__main__":
    port_scanner = PortScannerModule("127.0.0.1" , [22 , 135 , 443 , 445])
    sub_scanner = SubDomainModule("hedef.site.com" , ["admin", "api", "test", "login"])

    modules = [port_scanner , sub_scanner]

    print("=== NETPULSE FRAMEWORK ÇALIŞTIRILIYOR ===")
    for module in modules:
        module.run()
        print("-" * 40)

    try:
        bad_scanner = PortScannerModule("127.0.0.1" , [80 , 999999])
    except ValueError as e:
        print(e)
