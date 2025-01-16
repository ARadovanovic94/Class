class Student:
    def __init__(self, ime, prezime, broj_indeksa):
        self.ime = ime
        self.prezime = prezime
        self.broj_indeksa = broj_indeksa

    def informacije_o_studentu(self):
        return f"Student: {self.ime} {self.prezime} - {self.broj_indeksa}"


class Predmet:
    def __init__(self, naziv_predmeta):
        self.naziv_predmeta = naziv_predmeta


class Ispit(Predmet):
    def __init__(self, naziv_predmeta, datum_odrzavanja):
        super().__init__(naziv_predmeta)
        self.datum_odrzavanja = datum_odrzavanja



student = Student("Tom", "Davis", "555/55")

print(student.informacije_o_studentu())

predmet = Predmet("Matematika")

ispit = Ispit("Matematika", "20.01.2025")

print(f"Predmet: {ispit.naziv_predmeta}, Datum održavanja: {ispit.datum_odrzavanja}")