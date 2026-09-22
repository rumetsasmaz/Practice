import socket

def check_port(ip , port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((ip , port))    
    s.close()
    if result == 0:
        return True
    else:
        return False


target_ip = input("Enter A IP: ")
start_port = int(input("Enter A Start Port: "))
end_port = int(input("Enter A End Port: "))

open_ports = []


for port in range(start_port , end_port + 1):

    if check_port(target_ip , port) == True:
        print(f"[+] Port {port} Is OPEN")
        open_ports.append(port)
    else:
        print(f"[-] Port {port} Is CLOSED") 



print("\n--- RESULTS ---")
print(f"Open Ports: {open_ports}")

with open("port_results.txt" , "w") as file:
    file.write("--- PORT RESULTS ---\n")
    file.write(f"Open Ports: {open_ports}\n")
    