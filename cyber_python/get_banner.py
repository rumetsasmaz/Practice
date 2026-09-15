import socket

def get_banner(target_ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2.0)
    
    try:
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"[SUCCESS] Port {port}: OPEN")
            try:
              
                s.send(b"GET / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\n\r\n")
                banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
                if banner:
                    print(f"[BANNER] Service Response:\n{'-'*30}\n{banner}\n{'-'*30}")
                else:
                    print(f"[BANNER]  The port is open, but the service did not return a text-based banner..")
            except:
                print(f"[BANNER] Data could not be sent to this port, or the service is not providing a banner..")
        else:
            print(f"[FAILED] Port {port}: CLOSED")
            
    except Exception as e:
        print(f"[-] An error occurred: {e}")
    finally:

        s.close()

get_banner("127.0.0.1", 145)