# Program CircuitEquivalentSolver
    # program utama untuk menyelesaikan rangkaian ekuivalen thevenin
# KAMUS
    # Variabel
        # R1,R2,R3,R4,R5,Ri,Rf,V1,V2,V3 : string / integer { nilai komponen untuk ditampilkan di gambar }
        # View : boolean { flag yang menyatakan kondisi masih melihat-lihat rangkaian }
        # Choose : boolean { flag yang menyatakan kondisi masih memilih rangkaian }
        # k : integer { urutan template yang sedang dipilih }
        # Rth, Rth1, Rth2 : class : resistor
        # Vth, Vth1, Vth2  class : sumberTegangan
        # Rtemp , Vtemp : real { variabel sementara untuk input Rth1,Vth1 serta Rth2,Vth2 }
    # Fungsi/Prosedur
        # procedure clrscr()
            # prosedur untuk membersihkan layar
            # I.S. layar console BELUM dibersihkan
            # F.S. layar console TELAH dibersihkan
# REALISASI FUNGSI/PROSEDUR
def clrscr():
    # prosedur untuk membersihkan layar
    # KAMUS LOKAL
    # ALGORITMA
    system('cls')
    system('clear')
        # catatan : beberapa console seperti GIT BASH menggunakan clear untuk membersihkan layar

# ALGORITMA UTAMA
from os import system
from time import sleep
    # meng-import gambar rangkaian
from gambar_rangkaian.gambar_rangkaian0 import rangkaian0
from gambar_rangkaian.gambar_rangkaian1 import rangkaian1
from gambar_rangkaian.gambar_rangkaian2 import rangkaian2
from gambar_rangkaian.gambar_rangkaian3 import rangkaian3
from gambar_rangkaian.gambar_rangkaian4 import rangkaian4
from gambar_rangkaian.gambar_rangkaian5 import rangkaian5
from gambar_rangkaian.gambar_rangkaian6 import rangkaian6
from gambar_rangkaian.gambar_rangkaian7 import rangkaian7
from gambar_rangkaian.gambar_rangkaianThevenin import rangkaianThevenin
from gambar_rangkaian.gambar_rangkaianUtama import rangkaianUtama

from OOP.OOP import *

    # meng-import program penghitungan rangkaian ekuivalen Thevenin
from Module.circuit0 import circuit0
from Module.circuit1 import circuit1
from Module.circuit2 import circuit2
from Module.circuit3 import circuit3
from Module.circuit5 import circuit5
from Module.circuit6 import circuit6
    # meng-import modul-modul tambahan
from interface.interface import *

def main():
        # inisiasi variabel
    R1 = "R1"
    R2 = "R2"
    R3 = "R3"
    R4 = "R4"
    R5 = "R5"
    V1 = "V1"
    V2 = "V2"
    V3 = "V3"
    Ri = "Ri"
    Rf = "Rf"

    View= True
    clrscr()
        # pesan selamat datang
    print(hello_message)
    print(creator)
    print(separator)
    print("--- TEKAN ENTER ---")
    input()
    clrscr()
        # menampilkan template utama sebleum melihat-lihat rangkaian
    input("--- TEKAN ENTER untuk melihat rangkaian utama ---")
    rangkaianUtama()

    clrscr()
        # mulai melihat-melihat dan memilih rangkaian
    for k in range(1,3): # melakukan sebanyak dua kali karena rangkaian yang di-inputkan ada 2 template
        while View: #Loop untuk melihat Rangkaian yang tersedia
            print("Silakan tekan angka 1-7 untuk melihat rangkaian yang tersedia")
            print(f"Masukkan 99 Jika anda ingin memilih rangkaian untuk template {k}")
            print("***pilih 100 untuk keluar***")
            gambar = int(input(inp))
            if gambar == 1:
                image= rangkaian1(R1,R2,R3,V1)
                clrscr() #clrscr() akan meng-"Clear Screen" prompt agar lebih enak dilihat
            elif gambar == 2:
                image = rangkaian2(R1,R2,R3,R4,R5,V1)
                clrscr()
            elif gambar == 3:
                image = rangkaian3(R1,R2,R3,R4,V1)
                clrscr()
            elif gambar== 4:
                image = rangkaian4(R1,R2,R3,V1,V2,V3)
                clrscr()
            elif gambar== 5:
                image= rangkaian5(R1,R2,R3,R4,R5,V1)
                clrscr()
            elif gambar== 6:
                image= rangkaian6(R1,R2,R3,Ri,Rf,V1,V2,V3)
                clrscr()
            elif gambar== 7:
                image=rangkaian7(R1,R2,R3,V1,V2,V3)
                clrscr()
            elif gambar == 99: #Untuk melanjutkan ke proses pemilihan Rangkaian
                View=False
                clrscr()
            elif gambar == 100: #Untuk terminasi program
                clrscr()
                exit()
            else: #Jika Input Tidak Valid
                print("Input tidak Valid, Tekan Enter untuk melanjutkan")
                input()
                clrscr()

        Choose = True
        while Choose:
            print(f"Silakan masukan angka 1-7 untuk memilih rangkaian yang akan digunakan sebagai template {k}:")
            print("***pilih 0 untuk rangkaian kosong***")
            cmd=int(input(inp))
            if (cmd in range(0,8)): # user telah memilih rangkaian yang valid [no. 1 -- 7]
                Choose = False
            if cmd==1:
                image=rangkaian1(R1,R2,R3,V1) #Memperlihatkan Circuit 1 kembali
                Rtemp, Vtemp = circuit1() #Fungsi Circuit 1
                rangkaianThevenin(Vtemp,Rtemp)
                clrscr()
            elif cmd==2:
                image=rangkaian2(R1,R2,R3,R4,R5,V1) #Memperlihatkan Circuit 2 kembali
                Rtemp, Vtemp = circuit2() #Fungsi Circuit 2
                rangkaianThevenin(Vtemp,Rtemp)
                clrscr()
            elif cmd==3:
                image=rangkaian3(R1,R2,R3,R4,V1)
                Rtemp, Vtemp = circuit3()
                rangkaianThevenin(Vtemp,Rtemp)
                clrscr()
            elif cmd==4:
                print("Gunakan Fungsi Rangkaian 4")
            elif cmd==5:
                image=rangkaian5(R1,R2,R3,R4,R5,V1)
                Rtemp, Vtemp = circuit5()
                rangkaianThevenin(Vtemp,Rtemp)
                clrscr()
            elif cmd==6:
                image=rangkaian6(R1,R2,R3,Ri,Rf,V1,V2,V3)
                Rtemp, Vtemp = circuit6()
                rangkaianThevenin(Vtemp,Rtemp)
                clrscr()
            elif cmd==7:
                print("Gunakan Fungsi Rangkaian 7")
            elif cmd==0:
                image=rangkaian0()
                Rtemp, Vtemp = circuit0()
                clrscr()
            else:
                print("Input tidak valid, Tekan Enter untuk melanjutkan")
                input()
                clrscr()
            if k == 1 :
                Rth1 = resistor("Rth1",Rtemp)
                Vth1 = sumberTegangan("Vth1",Vtemp)
            elif k == 2 :
                Rth2 = resistor("Rth2",Rtemp)
                Vth2 = sumberTegangan("Vth2",Vtemp)

    # menghitung rangkaian ekuivalen secara keseluruhan dan mencetak rangkaian ekuivalen akhir
    Rth = resistor("Rth",Rth1.nilai+Rth2.nilai)
    Vth = sumberTegangan("Vth",Vth1.nilai+Vth2.nilai)
    clrscr()

    print("secara keseluruhan, rangkaian ekuivalen theveninnya adalah: ")
    Rth.display()
    Vth.display()
    print("TEKAN ENTER UNTUK MELIHAT RANGKAIAN EKUIVALEN AKHIR")
    input("")
    rangkaianThevenin(Vth1.nilai + Vth2.nilai,Rth1.nilai + Rth2.nilai)

main()

#untuk menjalankan: python3 thevenin.py
