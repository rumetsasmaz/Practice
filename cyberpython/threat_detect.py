def detect_threat(ip_list): 
    for ip in ip_list:
     if ip == "192.168.1.100":
        print(f"Threat Found {ip}")


ips = ["10.0.0.1", "192.168.1.100", "172.16.0.1"]

detect_threat(ips)