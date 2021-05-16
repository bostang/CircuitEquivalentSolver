import numpy as py

def circuit1():
    v1 = int(input("Masukkan nilai V1: "))
    r1 = int(input("Masukkan nilai R1: "))
    r2 = int(input("Masukkan nilai R2: "))
    r3 = int(input("Masukkan nilai R3: "))

    rth = ((r2*r3)/(r2+r3))+r1
    vth =(v1/r2)*((1/r1) + (1/r2))
    print("Nilai Resistor Ekivalen adalah: " + str(rth))
    print("Nilai Voltase Ekivalen adalah: " + str(vth))