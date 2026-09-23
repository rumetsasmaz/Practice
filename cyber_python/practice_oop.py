import socket

class Target:
    def __init__(self , ip , domain):
        self.ip = ip
        self.domain = domain
        self.is_alive = True
    def get_info(self):

        return f"Target Domain: {self.domain} | IP: {self.ip} | Active or Not: {self.is_alive}"


target1 = Target("192.168.1.1" , "mysite.com")
target1.get_info()

print(target1.get_info())