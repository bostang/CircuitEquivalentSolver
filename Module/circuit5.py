# Program rangkaian 5
# KAMUS
# Variabel
    # R1 : class : resistor
    # R2 : class : resistor
    # R3 : class : resistor
    # R4 : class : resistor
    # R5 : class : resistor
    # V1 : class : sumberTegangan
    # Vth : class : sumberTegangan
    # Rth : class : resistor
    # Va : real { tegangan di node A }
    # Vb : real { tegangan di node B }
    # koefisien : np.array
    # kanan : np.array
    # variabel : np.array { matriks solusi yaitu variabel = [va vb] }
        # catatan : Vth didefinisikan sebagai Vth = Va-Vb
    # val : real { variabel sementara untuk menginput nilai rangkaian }

# ALGORITMA UTAMA
    # meng-import library yang diperlukan untuk menyelesaikan persamaan matriks
import numpy as np
import scipy.linalg as la
from interface.interface import inp # meng-import parameter input : >>>
from OOP.OOP import *

def circuit5():
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

    print("Masukkan nilai R4: ")
    val = float(input(inp))
    R4 = resistor('R4',val)

    print("Masukkan nilai R5: ")
    val = float(input(inp))
    R5 = resistor('R5',val)

    print("Masukkan nilai V1: ")
    val = float(input(inp))
    V1 = sumberTegangan('V1',val)

        # menyelesaikan persamaan matriks menggunakan linear algebra module pada numpy
                # koefisien . variabel = R
    koefisien = np.array([[1,0],[1,-1]])
    kanan = np.array([V1.nilai-((R1.nilai*V1.nilai)/(R1.nilai+R2.nilai+R3.nilai+R4.nilai)),R3.nilai*(V1.nilai)/(R1.nilai+R2.nilai+R3.nilai+R4.nilai)])
    variabel = np.linalg.solve(koefisien,kanan)

    val = R5.nilai+(((R1.nilai+R2.nilai+R4.nilai)*R3.nilai)/(R1.nilai+R2.nilai+R4.nilai+R5.nilai))
    Rth = resistor('Rth',val)

    # Vth = kiri - kanan
    val = variabel[0] - variabel[1]
    Vth = sumberTegangan('Vth',val)
        # menampilkan output
    print("Nilai Resistor Ekivalen adalah:",Rth.nilai)
    print("Nilai Voltase Ekivalen adalah:",Vth.nilai)

    return (Rth.nilai,Vth.nilai) # mengembalikan nilai Rth dan Vth supaya bisa ditampilkan gambar rangkaian ekuivalennya
