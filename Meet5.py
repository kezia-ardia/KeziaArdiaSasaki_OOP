class DataAlumni:
    def __init__(self, tahun_lulus):
        self.tahun_lulus = tahun_lulus

    def info(self):
        return f"Lulus tahun {self.tahun_lulus}"


class DataAktif:
    def __init__(self, semester):
        self.semester = semester

    def info(self):
        return f"Semester {self.semester}"


class KTM(DataAktif):
    pass


class Ijazah(DataAlumni):
    pass


class Beasiswa(DataAktif):
    pass


class Clearance(DataAlumni, DataAktif):
    def __init__(self, tahun_lulus, semester):
        DataAlumni.__init__(self, tahun_lulus)
        DataAktif.__init__(self, semester)

    def info(self):
        return f"{DataAlumni.info(self)}, {DataAktif.info(self)}"


kartu = KTM(2)
ijazah = Ijazah(2024)
beasiswa = Beasiswa(3)
clear = Clearance(2023, 4)

print(kartu.info())
print(ijazah.info())
print(beasiswa.info())
print(clear.info())