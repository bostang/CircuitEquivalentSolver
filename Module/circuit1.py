# program rangkaian1
    # template rangkaian pertama dari program circuitEquivalentCircuit yang mau diselesaikan
# KAMUS
    # Variabel
        # R1 : class :resistor
        # R2 : class : resistor
        # R3 : class :resistor
        # V1 : class : sumberTegangan
        # val : real { variabel sementara untuk menginput nilai rangkaian }
# ALGORITMA UTAMA
    # meng-import library yang diperlukan untuk menyelesaikan persamaan matriks
import numpy as py
from interface.interface import inp # meng-import parameter input : >>>
from OOP.OOP import *

def circuit1():
        # menerima input user
    print("Masukkan nilai R1: ")
    val = float(input(inp))
    R1 = resistor('R1',val)

    print("Masukkan nilai R2: ")
    val = float(input(inp))
    R2 = resistor('R2',val)

    print("Masukkan nilai R3: ")
    val = float(input(inp))
    R3 = resistor('R3',val)

    print("Masukkan nilai V1: ")
    val = float(input(inp))
    V1 = sumberTegangan('V1',val)

    val = ((R2.nilai*R3.nilai)/(R2.nilai+R3.nilai))+R1.nilai
    Rth = resistor('Rth',val)

    val =(V1.nilai*R3.nilai)/((R2.nilai) + (R3.nilai))
    Vth = sumberTegangan('Vth',val)

    print("Nilai Resistor Ekivalen adalah:",Rth.nilai)
    print("Nilai Voltase Ekivalen adalah:",Vth.nilai)

    return (Rth.nilai,Vth.nilai) # mengembalikan nilai Rth dan Vth supaya bisa ditampilkan gambar rangkaian ekuivalennya
