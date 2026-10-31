import ipaddress
import socket
from logging import exception
while True:
    x = input("hedef ip:")
    try:
        network = ipaddress.ip_network(x.strip(), strict=False)
        if network.num_addresses == 1:
            ip_list = [str(network.network_address)]
        else:
            ip_list = [str(ip) for ip in network.hosts()]
        break
    except ValueError as e:
        print("hata olustu:", e)
        print("istenilen formatta giriniz")
        ip_list = []

y = int(input("baslangıc port:"))
z = int(input("bitis port:"))
print("Hedef ıp = {}\nbaslangıc port no= {}\nbitis port no = {} ".format(x,y,z))



for ip in ip_list:
    print("ip={} taranıyor".format(ip))
    for i in range(y, z + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            sonuc = s.connect_ex((ip, i))

            if sonuc == 0:
                print("{} portu acıktır".format(i))

            s.close()

        except exception:
            pass
    print("tarama işlemi bitti: {} ".format(ip))
    
