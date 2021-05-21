# program gambarRangkaian2
    # menggambar template rangkaian 2 menggunakan schemdraw
# KAMUS
    # d : schemdraw.drawing
# ALGORITMA UTAMA
import schemdraw
import schemdraw.elements as elm
#schemdraw.use('svg')

def rangkaian2(R1,R2,R3,R4,R5,V1):
        # menginisiasi rangkaian
    d = schemdraw.Drawing()

        # menambahkan elemen pada rangkaian
    d += elm.Dot().label('a',loc = 'top')
    d += elm.Line().down().length(1)
    d += elm.Line().left()
    d += elm.Resistor().down().length(6).label(R2,loc = 'top') # panjang satu komponen adalah 3, maka agar 2 kali lebih panjang, length = 6
    d += elm.Line().right()
    d += elm.SourceV().up().label(V1)
    d += elm.Resistor().up().label(R5,loc="bottom")
    d += elm.Resistor().right().label(R1,loc="top")
    d.push()

    d += elm.Resistor().down().length(6).label(R4,loc="top")
    d += elm.Resistor().left().label(R3,loc="bottom")

    d.pop()
    d += elm.Line().up().length(1)
    d += elm.Dot().label('b', loc = 'top')

        # menggambar rangkaian yang telah disusun
    d.draw()

    # catatan:
        # d.push() --> men-'save' koordinat sekarang supaya kita bisa kembali lagi nanti
        # d.pop() --> kembali ke koordinat yang telah kita simpan sebelumnya

        # trick ini sangat berguna untuk menggambar percabangan pada rangkaian
