# multiple inheritance & multilevel inheritance

class Mhsalumni:
    def lulus(self):
        print("mahasiswa ini lulus tahun 2025")
    
class Mhsaktif:
    def masuk(self):
        print("mahasiswa ini masuk tahun 2025")

# class child
class ktm(Mhsaktif):
    pass

class ijazah(Mhsalumni):
    pass

class beasiswa(Mhsalumni, Mhsaktif):
    pass

Ktm = ktm()
Ijazah = ijazah()
Beasiswa = beasiswa()

Ktm.masuk()
Ijazah.lulus()
Beasiswa.masuk()
Beasiswa.lulus()