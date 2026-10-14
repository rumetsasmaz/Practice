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


scanner = PortScannerModule("127.0.0.1" , [80 , 443])
scanner.run()