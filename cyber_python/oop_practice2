import socket


class Vulnerabilities:
    def __init__(self , service_name , port):
        self.service_name = service_name
        self.port = port
        self.is_Vulnerable = False
    def check_risk(self):
        if self.port == 21:
            self.is_Vulnerable = True
            return f"Critic: {self.service_name} Service Has Vulnerabilities!"
        else:
            return f"{self.service_name} Service Looking Safe"


vul1 = Vulnerabilities("FTP", 21)
print(vul1.check_risk())