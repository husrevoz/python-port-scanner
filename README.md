Python Port Scanner

Python ile geliştirilmiş basit bir port tarama aracı.

Bu projeyi Python öğrenirken socket programlama pratiği yapmak ve port taramanın nasıl çalıştığını anlamak için geliştirdim.

Özellikler
TCP port tarama
Multithreading desteği
CIDR desteği
Komut satırı parametreleri
Gereksinimler
Python 3
Kurulum

Projeyi bilgisayarınıza indirin:

bash
git clone https://github.com/husrevoz/python-port-scanner.git
cd python-port-scanner

Kullanım

Programın kullanılabilir parametrelerini görmek için:

bash
python3 portscannerv3.py --help

Öğrendiklerim
Python'da socket kullanımı
Temel ağ kavramları
Thread kullanımı
IP adresleri ve CIDR aralıkları
Komut satırı parametreleriyle çalışma
Uyarı

Bu proje eğitim amaçlı geliştirilmiştir. Yalnızca sahibi olduğunuz veya tarama izniniz bulunan ağlarda kullanın.
python PortScannerv4.py --hedef <IP/CIDR> [--port-range <BAŞLANGIÇ-BİTİŞ>] [--thread <SAYI>]
