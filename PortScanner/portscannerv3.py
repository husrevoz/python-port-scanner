import ipaddress
import socket
import sys
import argparse
from concurrent.futures import ThreadPoolExecutor


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
        self.start_scan()

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

    def start_scan(self):

        print(f"{self.hedef_ip} icin tarama islemi baslatiliyor")

        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            for ip, port in self.target_pairs:
                executor.submit(self.scan_single, ip, port)

        print("tarama islemi bitti")

if __name__ == "__main__":
    if len(sys.argv) < 5:

        sys.exit(1)

    hedef_ip = sys.argv[1]
    ilk_port = int(sys.argv[2])
    son_port = int(sys.argv[3])
    max_threads = int(sys.argv[4])

    PortScanner(hedef_ip, ilk_port, son_port, max_threads)