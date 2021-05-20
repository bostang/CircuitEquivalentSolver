# program rangkaian4
    # template rangkaian ke-empat dari program circuitEquivalentCircuit yang mau diselesaikan
# KAMUS
    # Variabel
        # R1 : class : resistor
        # R2 : class : resistor
        # R3 : class : resistor
        # V1 : class : sumberTegangan
        # V2 : class : sumberTegangan
        # V3 : class : sumberTegangan
        # Vth : class : sumberTegangan
        # Rth : class : resistor
        # i : real { arus pada loop yang didapat dengan KVL }
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

def circuit4():
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

    print("Masukkan nilai V2: ")
    val = float(input(inp))
    V2 = sumberTegangan('V2',val)

    print("Masukkan nilai V3: ")
    val = float(input(inp))
    V3 = sumberTegangan('V3',val)

        # menyelesaikan persamaan matriks menggunakan linear algebra module pada numpy
            # koefisien . variabel = R
    i = (V1.nilai+V2.nilai+V3.nilai)/(R1.nilai+R2.nilai+R3.nilai)
    koefisien = np.array([[-1,1],[1/R1.nilai,0]])
    kanan = np.array([i-V2.nilai,i])
    variabel = np.linalg.solve(koefisien,kanan)

    val = (R2.nilai*(R1.nilai+R3.nilai))/(R1.nilai+R2.nilai+R3.nilai)
    Rth = resistor('Rth',val)

    # Vth = kiri - kanan
    val = variabel[0] - variabel[1]
    Vth = sumberTegangan('Vth',val)

        # menampilkan output
    print("Nilai Resistor Ekivalen adalah:",Rth.nilai)
    print("Nilai Voltase Ekivalen adalah:",Vth.nilai)

    return (Rth.nilai,Vth.nilai) # mengembalikan nilai Rth dan Vth supaya bisa ditampilkan gambar rangkaian ekuivalennya
