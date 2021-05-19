# program gambarRangkaian0
    # menggambar template dasar [rangkaian kosong/trivial] menggunakan schemdraw
# KAMUS
    # d : schemdraw.drawing
# ALGORITMA UTAMA
import schemdraw
import schemdraw.elements as elm
#schemdraw.use('svg')

def rangkaian0():
        # menginisiasi rangkaian
    d = schemdraw.Drawing()

        # menambahkan elemen pada rangkaian
    d += elm.Dot().label('a',loc = 'right')
    d += elm.Line().left()
    d += elm.Dot().label('b',loc='left')

        # menggambar rangkaian yang telah disusun
    d.draw()
