def filter_safe_ports(port_list):
    safe_ports = []

    for port in port_list:
     if port != 21 and port != 23:
        safe_ports.append(port)
    return safe_ports

all_ports = [21 , 22 , 23 , 80 , 443 ]


print(filter_safe_ports(all_ports))
