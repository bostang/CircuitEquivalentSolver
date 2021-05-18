# program gambarRangkaian1
    # menggambar template rangkaian 1 menggunakan schemdraw
# KAMUS
    # Variabel
        # d : schemdraw.drawing
    # Fungsi/Prosedur
        # procedure rangkaianUtamaKosong ( input template1, template2 : integer)
            # mencetak kondisi rangkaian utama ketika belum di-isi temlate apapun
            # I.S. template 1 dan template 2 telah terdefinisi
            # F.S. rangkaian utama ketika kosong telah ditampilkan
        # procedure rangkaianUtamaSetengahLengkap ( input template1, template2 : integer)
            # mencetak kondisi rangkaian utama ketika telah di-isi tempalte 1
            # I.S. template 1 dan template 2 telah terdefinisi
            # F.S. rangkaian utama ketika setengah lengkap telah ditampilkan
        # procedure rangkaianUtamaLengap ( input template1, template2 : integer)
            # mencetak kondisi rangkaian utama ketika template 1 dan template 2 telah diisi
            # I.S. template 1 dan template 2 telah terdefinisi
            # F.S. rangkaian utama ketika lengkap telah ditampilkan
# ALGORITMA UTAMA
import schemdraw
import schemdraw.elements as elm
#schemdraw.use('svg')

def rangkaianUtama():
        # menginisiasi rangkaian
    d = schemdraw.Drawing()
        # menambahkan elemen pada rangkaian
    d += elm.Dot().label('a',loc = 'left')
    d += elm.Line().length(1)
    d += elm.RBox().linestyle('--').color('red').label("TEMPLATE 1").length(2)
    d += elm.Line().length(1)
    d += elm.RBox().linestyle('--').color('red').label("TEMPLATE 2").length(2)
    d += elm.Line().length(1)
    d += elm.Dot().label('b',loc = 'right')
        # menggambar rangkaian
    d.draw()

rangkaianUtama()
