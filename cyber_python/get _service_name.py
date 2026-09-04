def get_service_name(services , port):
    try:
        return services[port]
    except KeyError:
        return "Unknown Service" 

port_services = {
        20: "FTP Data Transfer",
        21: "FTP Control",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS"
    }

print(get_service_name(port_services, 22))
print(get_service_name(port_services, 443))
