def port_sorgula(port, sozluk):

    if port in sozluk:
        return f"{port} portu {sozluk[port]}: protokolu icin kullanilmaktadir."
    else:
        return f"{port} portu bilinen bir protokol icin kullanilmamaktadir."


bilinen_portlar = {
        80: "HTTP",
        443: "HTTPS",
        22: "SSH",
        21: "FTP",
        25: "SMTP",
    }



port = int(input("Port numarasini giriniz:"))
sonuc = port_sorgula(port, bilinen_portlar)
print(sonuc)

