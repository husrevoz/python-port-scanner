import ipaddress
import socket
from concurrent.futures import ThreadPoolExecutor

class portscan:
    def __init__(self,Hedefİp,baslangıcPort,sonPort,max_threads):
        self.Hip = Hedefİp
        self.bp=baslangıcPort
        self.sp = sonPort
        self.max_threads = max_threads

        try:
            network = ipaddress.ip_network(self.Hip.strip(), strict=False)
            if network.num_addresses == 1:
                self.ip_list = [str(network.network_address)]
            else:
                self.ip_list = [str(ip) for ip in network.hosts()]
        except ValueError as e:
            print("hata olustu:", e)
            return
        self.target_pairs = [
            (ip,port)
            for ip in self.ip_list
            for port in range(self.bp,self.sp+1)
        ]
        self.start_scan
def scan_single (self, ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        sonuc = s.connect_ex((ip, port))

        if sonuc == 0:
            print("{} portu acıktır".format(port))
        s.close()
    except Exception:
        pass

def start_scan(self):
    with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
        for ip, port in self.target_pairs:
            executor.submit(self.scan_single, ip, port)

if __name__ == "__main__":

    portscan("172.20.10.6/28",1,1024,50)