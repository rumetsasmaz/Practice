class BaseModule:
    def __init__(self , target):
        self.target = target

    def run(self):

        raise NotImplementedError

class PortScannerModule(BaseModule):
    def __init__(self , target , ports):

        super().__init__(target)
        self.ports = ports

    def run(self):
        print(f"[*] Starting Port Scan: {self.target}")
        try:

            for port in self.ports:

                if port == 443:
                    print(f"[+] Port {port}: Port Open (HTTPS)")
                else:
                    print(f"[-] Port {port}: Port Open")
        except Exception as e:
            print(f"[-] An error occurred during the scan {e}")

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
    target_host = "hedef.site.com"
port_scanner = PortScannerModule(target_host , [80 , 443 , 8080])
sub_scanner = SubDomainModule(target_host , ["admin", "api", "test", "login"])

modules = [port_scanner , sub_scanner]

print("=== NETPULSE FRAMEWORK ÇALIŞTIRILIYOR ===")
for module in modules:
    module.run()
    print("-" * 40)