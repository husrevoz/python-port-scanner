# Python Port Scanner

Python ile geliştirdiğim, nesne yönelimli (OOP) mimariye sahip, `argparse` ile parametre yönetimi sunan ve `ThreadPoolExecutor` ile paralel tarama yapabilen bir CLI port tarayıcı.

Tekil IP adreslerinin yanı sıra CIDR bloklarını (`/24`, `/16` vb.) otomatik ayrıştırarak ağ üzerindeki açık portları hızlıca tespit eder.

## Özellikler

* **Paralel Tarama:** Multi-threading sayesinde portları eşzamanlı ve hızlı bir şekilde tarar.
* **Esnek Port Aralığı:** `--port-range` parametresi ile ister tek bir portu (`80`), ister belirli bir aralığı (`20-1024`) tarayabilirsiniz.
* **CIDR ve Ağ Desteği:** `ipaddress` kütüphanesi ile alt ağ bloklarını otomatik çözümler.
* **Gelişmiş CLI:** `argparse` altyapısı sayesinde parametreleri isimleriyle (`--hedef`, `--port-range`, `--thread`) kolayca yönetmenizi sağlar.

## Kullanım

Herhangi bir harici kütüphane bağımlılığı yoktur. Terminalden çalıştırmak için:

```bash
python PortScannerv4.py --hedef <IP/CIDR> [--port-range <BAŞLANGIÇ-BİTİŞ>] [--thread <SAYI>]
