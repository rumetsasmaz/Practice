def scan_ports(port_list):
    open_ports = []
    for port in port_list:
      if port == 80 or port == 443:
          open_ports.append(port)

    return open_ports



ports = [21 , 22 , 80 , 443 , 8080]
result = scan_ports(ports)

print(result)