def extract_local_ips(log_list):
    local_ip_logs = []
    for log in log_list:
        if "192.168." in log or "10." in log or "172.16." in log:
            local_ip_logs.append(log)
    return local_ip_logs

logs = [
    "CONN FROM 192.168.1.15",
    "CONN FROM 10.0.0.1",
    "CONN FROM 192.168.1.50",
    "CONN FROM 172.16.0.1"
]

print(extract_local_ips(logs))