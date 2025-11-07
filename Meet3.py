class Person:
    def __init__(self, nama="", usia=0):
        self.nama = nama
        self.usia = usia

    def infoDosen(self):
        return self.nama + " sedang mengajar mata kuliah " + self.mata_kuliah

    def infoMahasiswa(self):
        return self.nama + " sedang belajar di jurusan " + self.jurusan


class Dosen(Person):
    def __init__(self, nidn):
        self.nidn = nidn


class Mahasiswa(Person):
    def __init__(self, nim):
        self.nim = nim


dosen1 = Dosen("123456")
dosen1.nama = "Edy"
dosen1.usia = 17
dosen1.mata_kuliah = "Pemrograman Berorientasi Objek"

print("==== Data Dosen ====")
print("Nama:", dosen1.nama)
print("Usia:", dosen1.usia)
print("NIDN:", dosen1.nidn)
print("Mata Kuliah:", dosen1.mata_kuliah)
print(dosen1.infoDosen())

print()

mhs1 = Mahasiswa("24241169")
mhs1.nama = "Kezia Ardia Sasaki"
mhs1.usia = 19
mhs1.jurusan = "Pendidikan Teknologi Informasi"

print("==== Data Mahasiswa ====")
print("Nama:", mhs1.nama)
print("Usia:", mhs1.usia)
print("NIM:", mhs1.nim)
print("Jurusan:", mhs1.jurusan)
print(mhs1.infoMahasiswa())