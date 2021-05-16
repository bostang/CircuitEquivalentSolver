from os import system
from gambar_rangkaian.gambar_rangkaian1 import rangkaian1
from gambar_rangkaian.gambar_rangkaian2 import rangkaian2
from gambar_rangkaian.gambar_rangkaian3 import rangkaian3
from gambar_rangkaian.gambar_rangkaian4 import rangkaian4
from gambar_rangkaian.gambar_rangkaian5 import rangkaian5
from gambar_rangkaian.gambar_rangkaian6 import rangkaian6
from gambar_rangkaian.gambar_rangkaian7 import rangkaian7
from Module.circuit1 import circuit1
from Module.circuit2 import circuit2


def main():
    View= True
    print("Selamat Datang Di Program Thevenin Equivalent Solver!")
    while View: #Loop untuk melihat Rangkaian yang tersedia
        print("Silakan tekan angka 1-7 untuk melihat rangkaian yang tersedia")
        gambar = int(input("Masukkan 99 Jika anda ingin memilih rangkaian: ")) # 99 Untuk Memilih Rangkaian
        if gambar == 1:
            image= rangkaian1()
            system("cls") #System("cls") akan meng-"Clear Screen" prompt agar lebih enak dilihat
        elif gambar == 2:
            image = rangkaian2()
            system("cls")
        elif gambar == 3:
            image = rangkaian3()
            system("cls")
        elif gambar== 4:
            image = rangkaian4()
            system("cls")
        elif gambar== 5:
            image= rangkaian5()
            system("cls")
        elif gambar== 6:
            image= rangkaian6()
            system("cls")
        elif gambar== 7:
            image=rangkaian7()
            system("cls")
        elif gambar == 99: #Untuk melanjutkan ke proses pemilihan Rangkaian
            View=False
            system("cls")
        else: #Jika Input Tidak Valid
            print("Input tidak Valid, Tekan Enter untuk melanjutkan")
            input()
            system("cls")

    cmd=int(input("Silakan masukan angka 1-7 untuk memilih rangkaian yang akan digunakan: "))
    if cmd==1:
        image=rangkaian1() #Memperlihatkan Circuit 1 kembali
        circuit1() #Fungsi Circuit 1
    elif cmd==2:
        image=rangkaian2() #Memperlihatkan Circuit 2 kembali
        circuit2() #Fungsi Circuit 2
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

