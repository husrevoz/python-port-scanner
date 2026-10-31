#!/usr/bin/env python3
import ipaddress
import socket
import sys
import argparse
from concurrent.futures import ThreadPoolExecutor

__version__=1.1.1
class PortScanner:

    def __init__(self, hedef_ip, ilk_port, son_port, max_threads):
        self.hedef_ip = hedef_ip
        self.ilk_port = ilk_port
        self.son_port = son_port
        self.max_threads = max_threads

        try:
            network = ipaddress.ip_network(hedef_ip.strip(), strict=False)
            if network.num_addresses == 1:
                self.ip_list = [str(network.network_address)]
            else:
                self.ip_list = [str(ip) for ip in network.hosts()]
        except ValueError as e:
            print("hata alindi:",e)
            return

        self.target_pairs = [
            (ip, port)
            for ip in self.ip_list
            for port in range(self.ilk_port, self.son_port + 1)
        ]
        self.tarama()

    def scan_single(self, ip, port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            sonuc = s.connect_ex((ip, port))

            if sonuc == 0:
                print(f"Açık Port: {ip}:{port}")

            s.close()
        except Exception:
            pass

    def tarama(self):

        print(f"{self.hedef_ip} icin tarama islemi baslatiliyor")

        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            for ip, port in self.target_pairs:
                executor.submit(self.scan_single, ip, port)

        print("tarama islemi bitti")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Gelişmiş Port Tarayıcı",formatter_class=argparse.RawTextHelpFormatter)
    
    parser.add_argument("--v","--version",action="version",version="%(prog)s v{__version__}",help="program sürüm bilgisi gösterir.")

    parser.add_argument("--hedef", type=str, required=True, help="Hedef IP adresi veya CIDR bloğu (ör: 1.1.1.1 veya 1.1.1.1/24)")

    parser.add_argument("--port-range", type=str, default="1-1024", help="Tarayacak port aralığı (ör: 68-6800)")
    
    parser.add_argument("--thread", type=int, default=20 ,help="Eşzamanlı thread sayısı (ör: 20)")

    args = parser.parse_args()

    try:
        if "-" in args.port_range:
            ilk_port, son_port = map(int, args.port_range.split("-"))
        else:
            ilk_port = son_port = int(args.port_range)
    except ValueError:
        print("Hata: --port-range değeri '68-6800' veya '68' şeklinde olmalıdır!")
        sys.exit(1)

    PortScanner(args.hedef,ilk_port,son_port, args.thread)
       
