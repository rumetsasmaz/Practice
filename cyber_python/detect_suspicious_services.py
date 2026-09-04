def detect_suspicious_services(active_services, allowed_ports):
    suspicious_ports = {}
    for port, service in active_services.items():
        if port not in allowed_ports:
            suspicious_ports[port] = service
    return suspicious_ports

active_services = {

    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    4444: "Metasploit Shellcode", 
    6667: "IRC Botnet Connection",
    3389: "RDP"
}

allowed_ports = [22, 80, 443, 3306, 5432, 3389, 6379, 27017]

suspicious_services = detect_suspicious_services(active_services, allowed_ports)

print(suspicious_services)