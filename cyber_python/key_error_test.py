def get_server_ip(server_dict , server_name):
    try:
        return server_dict[server_name]
    except KeyError:
        return "Error: Server name not found"

servers = {"web": "192.168.1.100", "db": "192.168.1.20"}

print(get_server_ip(servers, "web"))
print(get_server_ip(servers, "db"))
print(get_server_ip(servers, "app"))
