import numpy as py

def circuit1():
    V1 = int(input("Masukkan nilai V1: "))
    R1 = int(input("Masukkan nilai R1: "))
    R2 = int(input("Masukkan nilai R2: "))
    R3 = int(input("Masukkan nilai R3: "))

    Rth = ((R2*R3)/(R2+R3))+R1
    Vth =(V1/R2)*((1/R1) + (1/R2))
    print("Nilai Resistor Ekivalen adalah: " + str(Rth))
    print("Nilai Voltase Ekivalen adalah: " + str(Vth))
