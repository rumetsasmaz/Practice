def cyber_security_analyzer(log_list , min_pass_len):
    threat_logs = []
    safe_logs = []

    for log in log_list:
        if "192.168.1.100" in log or "21" in log or "ATTACK" in log:
            threat_logs.append(log)
        elif "PASS:" in log:
            password = log.split("PASS: ")[1]
            if len(password) < min_pass_len:
             threat_logs.append(log) 
        else:
            safe_logs.append(log)   

    return threat_logs , safe_logs

logs = [
    "USER: admin - PASS: secret123",        
    "USER: guest - PASS: 123",              
    "SRC: 192.168.1.100 - PORT: 80",        
    "SRC: 10.0.0.5 - PORT: 21",            
    "SRC: 172.16.0.1 - PORT: 443",          
    "ALERT: SYSTEM ATTACK DETECTED"      
]

threats, safes = cyber_security_analyzer(logs, 8)

print("---TEHTIT LOGLARI---")
print(threats)
print("---GUVENLI LOGLAR---")
print(safes)
        