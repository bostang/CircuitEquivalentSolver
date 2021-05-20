# Program OOP
    # memanfaat konsep OOP untuk membuat class komponen rangkaian
# KAMUS
    # Variabel
    # Kelas
        # class Komponen
            # memodelkan komponen rangkaian secara umum
        # class resistor
            # memodelkan resistor
        # class sumberTegangan
            # memodelkan sumber tegangan
# ALGORITMA UTAMA

class komponen:
    def __init__(self,nama,nilai):
        self.nama = nama
        self.nilai = nilai
        self.satuan = ""
    def display(self):
        print(self.nama,"=",self.nilai,self.satuan)

class resistor(komponen): # sebuah class bernama resistor yang mewarisi atribut dari class komponen
    def __init__(self,nama,nilai):
        super().__init__(nama,nilai)
        self.satuan = "Ohm"

        # nilai konduktansi, dipakai di penghitungan linear algebra
        if self.nilai == 0.0:
            self.g = float('inf')
        else:
            self.g = 1 / self.nilai

class sumberTegangan(komponen): # sebuah class bernama sumberTegangan yang mewarisi atribut dari class komponen
    def __init__(self,nama,nilai):
        super().__init__(nama,nilai)
        self.satuan = "V"