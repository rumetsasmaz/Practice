def connect_to_target(ip):
    try:
        if ip == "127.0.0.1":
            print("Connected to localhost")
        else:
            raise ConnectionError("Unable to connect to the target IP address.")
    except ConnectionError as e:
        print(f"Connection failed: {e}")
    else:
        print(f"Successfully connected to {ip}")
    finally:
        print("Connection attempt finished.")


print("Testing connection to localhost:")
connect_to_target("127.0.0.1")
print("\nTesting connection to an invalid IP:")
connect_to_target("198.168.1.1")
