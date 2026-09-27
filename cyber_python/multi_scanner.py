import socket

class BaseScanner:

    def __init__(self , target_ip ):
        self.target_ip = target_ip
        self.logs = []

    def log(self , message):
        formatted_msg = f"[{self.target_ip}] {message}"
        self.logs.append(formatted_msg)
        print(formatted_msg)

class PortScanner(BaseScanner):

    def __init__(self , target_ip , ports_to_scan):
       
        super().__init__(target_ip)
        self.open_ports = []
        self.ports_to_scan = ports_to_scan

    def scan(self):
        self.log("Startded Port Scan")

        for port in self.ports_to_scan:

            try:

                s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
                s.settimeout(0.5)
                result = s.connect_ex((self.target_ip , port))
                s.close()

                if result == 0:
                  self.open_ports.append(port)
                  self.log(f"Port {port} OPEN!")
                else:
                    self.log(f"Port {port} CLOSED!")

            except KeyboardInterrupt:
                self.log("Stopped By The User")
                break
            except socket.error:
                self.log("Port {port} Connection Error")

class WebReconScanner(BaseScanner):

        def check_http_banner(self , port=80):

            self.log(f"Port {port} Querying HTTP banner on...")

            try:

                s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
                s.settimeout(1.0)
                result = s.connect_ex((self.target_ip , port))
                request = f"HEAD / HTTP/1.1\r\nHost: {self.target_ip}\r\n\r\n"
                s.send(request.encode())
                response = s.recv(1024).decode(errors="ignore")
                s.close()

                if "Server:" in response:
                    for line in response.split("\r\n"):
                        if line.startswith("Server"):
                            self.log(f"Server Information Retrieved -> {line}")
                else:
                    self.log("HTTP response received, but the Server header was not found.")

            except Exception as e:
                self.log(f"Banner could not be retrieved. (Error: {e})") 


if __name__ == "__main__":
    target = "127.0.0.1"

    print("=== 1. PORT SCANNER TEST ===")
    p_scanner = PortScanner(target, [80, 135, 443, 445])
    p_scanner.scan()

    print("\n=== 2. WEB RECON TEST ===")
    w_scanner = WebReconScanner(target)
    w_scanner.check_http_banner(80)

    print("\n=== LOG GEÇMİŞİ (Port Scanner) ===")
    print(p_scanner.logs)