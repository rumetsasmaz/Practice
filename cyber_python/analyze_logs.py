def analyze_logs(log_list):
    suspicious_logs = []

    for log in log_list:
     if "192.168.1.100" in log or "21" in log:
        suspicious_logs.append(log)

    return suspicious_logs

network_logs = [
    "10.0.0.1 - 80",
    "192.168.1.100 - 22",
    "172.16.0.5 - 21",
    "192.168.1.50 - 443"
]

print(analyze_logs(network_logs))