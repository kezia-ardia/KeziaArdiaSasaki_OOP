class kendaraan :
    def __init__(self, merk, model, warna, cc, kondisi_mesin, surat2, harga):
        self.merk = merk
        self.model = model
        self.warna = warna
        self.cc = cc
        self.kondisi_mesin = kondisi_mesin
        self.surat2 = surat2
        self.harga = harga

    def tampilkan_info(self):
        print(f"merk           : {self.merk}")
        print(f"model          : {self.model}")
        print(f"warna          : {self.warna}")
        print(f"cc             : {self.cc} cc")
        print(f"kondisi mesin  : {self.kondisi_mesin}")
        print(f"surat-surat    : {self.surat2}")
        print(f"harga          : Rp{self.harga:,}")

mobil = kendaraan(
    merk="mitsubishi",
    model="pajero sport",
    warna="putih",
    cc=2400,
    kondisi_mesin="Baik",
    surat2="Lengkap (STNK & BPKB)",
    harga=600000000
)

motor = kendaraan(
    merk="honda",
    model="scoopy",
    warna="putih",
    cc=150,
    kondisi_mesin="baik",
    surat2="lengkap",
    harga="22000000"
)
mobil.tampilkan_info()
motor.tampilkan_info()