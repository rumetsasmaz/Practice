import socket

class BaseScanner:


    def __init__(self , target_ip ):
        self.target_ip = target_ip
        self.logs = []
    
    def log(self , message):

        formatted_msg = f"[{self.target_ip}] {message}"
        self.logs.append(formatted_msg)
        print(formatted_msg)


class DNSReconScanner(BaseScanner):

    def check_dns_records(self):

        self.log("Checking DNS Records...")

        try:
            socket.setdefaulttimeout(2)
            result = socket.gethostbyaddr(self.target_ip)
            self.log(f"DNS Records Found: {result[0]}")
        except socket.herror:
            self.log("No DNS Records Found")


if __name__ == "__main__":
    
    target_dns = "8.8.8.8"

dns_scanner = DNSReconScanner(target_dns)
dns_scanner.check_dns_records()