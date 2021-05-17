# Program CircuitEquivalentSolver
    # program utama untuk menyelesaikan rangkaian ekuivalen thevenin
# KAMUS
    # Variabel
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
    # meng-import gambar rangkaian
from gambar_rangkaian.gambar_rangkaian1 import rangkaian1
from gambar_rangkaian.gambar_rangkaian2 import rangkaian2
from gambar_rangkaian.gambar_rangkaian3 import rangkaian3
from gambar_rangkaian.gambar_rangkaian4 import rangkaian4
from gambar_rangkaian.gambar_rangkaian5 import rangkaian5
from gambar_rangkaian.gambar_rangkaian6 import rangkaian6
from gambar_rangkaian.gambar_rangkaian7 import rangkaian7
    # meng-import program penghitungan rangkaian ekuivalen Thevenin
from Module.circuit1 import circuit1
from Module.circuit2 import circuit2
    # meng-import variabel tulisan-tulisan ASCII
from interface.interface import *

def main():
    View= True
    clrscr()
    print(hello_message)
    print(creator)
    print(separator)
    while View: #Loop untuk melihat Rangkaian yang tersedia
        print("Silakan tekan angka 1-7 untuk melihat rangkaian yang tersedia")
        print("Masukkan 99 Jika anda ingin memilih rangkaian")
        print("***pilih 100 untuk keluar***")
        gambar = int(input(">>> ")) # 99 Untuk Memilih Rangkaian
        if gambar == 1:
            image= rangkaian1()
            clrscr() #clrscr() akan meng-"Clear Screen" prompt agar lebih enak dilihat
        elif gambar == 2:
            image = rangkaian2()
            clrscr()
        elif gambar == 3:
            image = rangkaian3()
            clrscr()
        elif gambar== 4:
            image = rangkaian4()
            clrscr()
        elif gambar== 5:
            image= rangkaian5()
            clrscr()
        elif gambar== 6:
            image= rangkaian6()
            clrscr()
        elif gambar== 7:
            image=rangkaian7()
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

    cmd=int(input("Silakan masukan angka 1-7 untuk memilih rangkaian yang akan digunakan: "))
    if cmd==1:
        image=rangkaian1() #Memperlihatkan Circuit 1 kembali
        circuit1() #Fungsi Circuit 1
        clrscr()
    elif cmd==2:
        image=rangkaian2() #Memperlihatkan Circuit 2 kembali
        circuit2() #Fungsi Circuit 2
        clrscr()
    elif cmd==3:
        print("Gunakan Fungsi Rangkaian 3") # Rangkaian 3 sampai 7 to be added soon
    elif cmd==4:
        print("Gunakan Fungsi Rangkaian 4")
    elif cmd==5:
        print("Gunakan Fungsi Rangkaian 5")
    elif cmd==6:
        print("Gunakan Fungsi Rangkaian 6")
    elif cmd==7:
        print("Gunakan Fungsi Rangkaian 7")
    else:
        print("Input tidak valid.")

main()

#untuk menjalankan: python3 thevenin.py
