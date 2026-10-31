# Python Port Scanner

Python ile geliştirdiğim, nesne yönelimli (OOP) mimariye sahip ve `ThreadPoolExecutor` ile paralel tarama yapabilen bir CLI port tarayıcı.

Tekil IP adreslerinin yanı sıra CIDR bloklarını (`/24`, `/16` vb.) otomatik ayrıştırarak ağ üzerindeki açık portları hızlıca tespit eder.

## Özellikler

* **Paralel Tarama:** Çoklu iş parçacığı (multi-threading) sayesinde portları sırayla beklemek yerine eşzamanlı tarar.
* **CIDR ve Ağ Desteği:** `ipaddress` kütüphanesi ile alt ağ bloklarını otomatik çözümler.
* **CLI Kullanımı:** Terminalden verilen argümanlarla doğrudan çalışır, soru sorma adımlarını atlar.

## Kullanım

Herhangi bir harici kütüphane bağımlılığı yoktur. Terminalden 4 argüman vererek çalıştırabilirsiniz:

```bash
python updatePortScan.py <IP/CIDR> <Başlangıç Port> <Bitiş Port> <Thread Sayısı>
