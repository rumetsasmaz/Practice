def get_port_by_index(port_list, index):
    try:
        return port_list[index]
    except IndexError:
        return "Error: Invalid list index"


ports = [22, 80, 443, 8080]

print(get_port_by_index(ports, 2))  
print(get_port_by_index(ports, 5))
print(get_port_by_index(ports, -1))
print(get_port_by_index(ports, 0))