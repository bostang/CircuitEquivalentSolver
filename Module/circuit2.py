# program rangkaian1
    # rangkaian pertama dari program circuitEquivalentCircuit yang mau diselesaikan
# KAMUS
    # Variabel
        # R1 : real
        # R2 : real
        # R3 : real
        # R4 : real
        # R5 : real
        # V1 : real
        # Vth : real
        # Rth : real
        # Va : real { tegangan di node A }
        # Vb : real { tegangan di node B }
        # koefisien : np.array
        # kanan : np.array
        # variabel : np.array { matriks solusi yaitu variabel = [va vb] }
            # catatan : Vth didefinisikan sebagai Vth = Va-Vb
# ALGORITMA UTAMA
    # meng-import library yang diperlukan untuk menyelesaikan persamaan matriks
import numpy as np
import scipy.linalg as la

    # menerima input user
def circuit2():
    R1 = float(input("Masukkan nilai R1: "))
    R2 = float(input("Masukkan nilai R2: "))
    R3 = float(input("Masukkan nilai R3: "))
    R4 = float(input("Masukkan nilai R4: "))
    R5 = float(input("Masukkan nilai R5: "))
    V1 = float(input("Masukkan nilai V1: "))

        # menyelesaikan persamaan matriks menggunakan linear algebra module pada numpy
                # koefisien . variabel = R
    koefisien = np.array([[1/R1,-((1/R1)+1/(R3+R4))],[(1/R1)+(1/R2)+(1/R5),(-1/R1)]])
    kanan = np.array([0,V1/R5])
    variabel = np.linalg.solve(koefisien,kanan)

    Rth = (R1*((R2*R5)/(R2+R5)+R3+R4))/(R1+R3+R4+(R2*R5/(R2+R5)))
    # Vth = kiri - kanan
    Vth = variabel[0] - variabel[1]

        # menampilkan output
    print("Nilai Resistor Ekivalen adalah:",Rth)
    print("Nilai Voltase Ekivalen adalah:",Vth)