import numpy as py
from interface.interface import inp # meng-import parameter input : >>>

def circuit1():
    print("Masukkan nilai R1: ")
    R1 = float(input(inp))

    print("Masukkan nilai R2: ")
    R2 = float(input(inp))

    print("Masukkan nilai R3: ")
    R3 = float(input(inp))

    print("Masukkan nilai V1: ")
    V1 = float(input(inp))

    Rth = ((R2*R3)/(R2+R3))+R1
    Vth =(V1/R2)*((1/R1) + (1/R2))
    print("Nilai Resistor Ekivalen adalah: " + str(Rth))
    print("Nilai Voltase Ekivalen adalah: " + str(Vth))
