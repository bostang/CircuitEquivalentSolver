# program gambarRangkaian0
    # menggambar template dasar [rangkaian kosong/trivial] menggunakan schemdraw
# KAMUS
    # d : schemdraw.drawing
# ALGORITMA UTAMA
import schemdraw
import schemdraw.elements as elm
#schemdraw.use('svg')

def rangkaian1(R1,R2,R3,V1):
        # menginisiasi rangkaian
    d = schemdraw.Drawing()

        # menambahkan elemen pada rangkaian
    d += elm.Dot().label('a',loc = 'right')
    d += elm.Wire().left().label(R1,loc="bottom")
    d += elm.Dot().label('b',loc='left')

        # menggambar rangkaian yang telah disusun
    d.draw()
