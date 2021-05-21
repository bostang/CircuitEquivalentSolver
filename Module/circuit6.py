# Mario Jeiba - 16520280
# Circuit Equivalent Solver, Circuit 6

from numpy import linalg
from interface.interface import inp
from OOP.OOP import *
_inf = float("inf")     # nilai tak hingga

# ================================================
# Circuit 6:
#                      n2
#               |------|------|---Rf---[+] nf
#               R1     R2     R3
#               |      |      |
#              (V1)   (V2)   (V3)
# ni [-]---Ri---|------|------|
#                      n1
# ================================================
# Req = Ri + (R1||R2||R3) + Rf
# Veq = V[nf] - V[ni]       V[nf] = V[n2]
#     = V[n2] - 0           V[ni] = 0
# ================================================
# Input:
#   Ri, R1, R2, R3, Rf    : resistor
#   V1, V2, V3            : sumberTegangan
# Output:
#   Req, Veq              : float
# ================================================

def promptvalue(var: str):
    """
    Membuat dialog untuk input nilai elemen.

    User input:
        val         : float     - nilai elemen masukan user.
    Output:
        val         : float
    """

    print("Masukkan nilai %s" % var)
    return float(input(inp))

def std_Veq(G1, G2, G3, V1, V2, V3):
    """
    Mencari Veq menggunakan konduktansi dan matriks.

    Input:
        G1, G2, G3  : float     - diambil dari resistor.g;
        V1, V2, V3  : float     - diambil dari sumberTegangan.nilai
    Output:
        Veq         : float     - tegangan ekivalen rangkaian
    """

    # Veq = V[nf] - V[ni] = V[n2] - 0
    # matrix_left * matrix_solution     = matrix_right
    # [-(G1+G2+G3)  G1  G2  G3] [V[n2]] = [0 ]
    # [ 0           1   0   0 ] [V[1] ] = [V1]
    # [ 0           0   1   0 ] [V[2] ] = [V2]
    # [ 0           0   0   1 ] [V[3] ] = [V3]

    # Gp : Konduktansi total pada bagian paralel
    Gp = G1 + G2 + G3

    matrix_left = [
        [-Gp, G1, G2, G3],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ]
    matrix_right = [
        0, V1, V2, V3
    ]
    matrix_solution = linalg.solve(matrix_left, matrix_right)

    # V[n2] = V[nf] adalah indeks ke-0 array solusi
    return matrix_solution[0]

def zero_res_Veq(G1, G2, G3, V1, V2, V3):
    """
    Mencari Veq jika pada bagian paralel terdapat resistor nol
    sehingga Veq = V cabang resistor nol tersebut.

    Input:
        G1, G2, G3  : float     - diambil dari resistor.g;
        V1, V2, V3  : float     - diambil dari sumberTegangan.nilai
    Output:
        Veq         : float     - tegangan ekivalen rangkaian
    Raise:
        ValueError  : jika pada bagian paralel terdapat >1 resistor nol.
    """

    Veq = None
    for g, v in ((G1, V1), (G2, V2), (G3, V3)):
        if g == _inf:
            if Veq is not None:
                # Veq sudah terisi Vs sebelumnya: terdapat >1 resistor nol
                raise ValueError("Two or more voltage sources directly in parallel")
            else:
                # Veq belum terisi: resistor nol pertama
                Veq = v
    return Veq

def circuit6():
    """
    Program penghitungan rangkaian ekivalen model Circuit 6.

    User input:
        R1, R2, R3  : resistor          - resistor bagian paralel.
        Ri, Rf      : resistor          - resistor bagian ujung.
        V1, V2, V3  : sumberTegangan    - sumber di bagian paralel.
    Output:
        Req, Veq    : float             - nilai terhitung resistor dan sumber
                                          tegangan ekivalen.
    Raise:
        ValueError  : jika pada bagian paralel terdapat >1 resistor nol.
    """

    # input variabel dari user
    R1 = resistor("R1", promptvalue("R1"))
    R2 = resistor("R2", promptvalue("R2"))
    R3 = resistor("R3", promptvalue("R3"))
    Ri = resistor("Ri", promptvalue("Ri"))
    Rf = resistor("Rf", promptvalue("Rf"))
    V1 = sumberTegangan("V1", promptvalue("V1"))
    V2 = sumberTegangan("V2", promptvalue("V2"))
    V3 = sumberTegangan("V3", promptvalue("V3"))

    # menghitung resistansi ekivalen rangkaian
    Gp = R1.g + R2.g + R3.g                 # tak hingga jika terdapat resistor nol
    Req_value = Ri.nilai + (1 / Gp) + Rf.nilai    # 1 / Gp = 0 jika terdapat resistor nol

    # menghitung tegangan ekivalen rangkaian
    Veq_elmts = (R1.g, R2.g, R3.g, V1.nilai, V2.nilai, V3.nilai)
    if Gp == _inf:
        # terdapat resistor nol, gunakan analisis resistor nol
        Veq_value = zero_res_Veq(*Veq_elmts)
    else:
        # tidak terdapat resistor nol, gunakan analisis biasa
        Veq_value = std_Veq(*Veq_elmts)

    # program selesai
    print("Nilai Resistor Ekivalen adalah: %f" % Req_value)
    print("Nilai Voltase Ekivalen adalah: %f" % Veq_value)
    return Req_value, Veq_value

if __name__ == "__main__":
    circuit6()
