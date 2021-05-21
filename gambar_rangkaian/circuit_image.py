# program cetakGambar
    # program python utuk mencetak gambar dari PC ke python console
# KAMUS
    # Variabel
        # img : string { gambar yang ingin dicetak }
# ALGORITMA UTAMA
def printImage(title):
    # mencetak gambar pada python. contoh penggunaan : printImage('gambar1.png') [kondisi : gambar1.png berada dalam 1 folder dengan file ini ]
    # KAMUS LOKAL
    # ALGORITMA
    ##%matplotlib inline
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    img = mpimg.imread(title)
    imgplot = plt.imshow(img)
        # menyembunyikan plot-axis dan gridline
    plt.grid(False)
    plt.axis('off')
        # menampilkan gambar
    plt.show()

        # catatan : %matplotlib inline ditambahkan supaya tidak ada pesan dari matplotlib

