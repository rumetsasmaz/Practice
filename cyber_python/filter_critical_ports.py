def filter_critical_ports(services ,critical_list):
    critical_found = {}
    for port , service in services.items():
        if port in critical_list:
            critical_found[port] = service
    return critical_found

critical_ports = [22,  23  ,80, 443, 3306, 5432, 6379, 27017]

services = {
    22: "SSH",
    23: "Telnet",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    5432: "PostgreSQL",
    6379: "Redis",
    27017: "MongoDB"
}

print(filter_critical_ports(services , critical_ports))