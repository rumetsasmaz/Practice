known_ports = {
    80: "HTTP",
    443: "HTTPS",
    22: "SSH",
    21: "FTP",
    25: "SMTP",
    23: "Telnet"

}

def port_inquery(port, port_dict):
    if port in port_dict:
        return f"{port} number is assigned to the {port_dict[port]} service"
    else:
        return f"{port} number is assigned to an unknown service"

port = int(input("Enter port number: "))
output = port_inquery(port, known_ports)
print(output)

# NEW SECTION — save result to file
with open("port_results.txt", "a", encoding="utf-8") as file:
    file.write(output + "\n")