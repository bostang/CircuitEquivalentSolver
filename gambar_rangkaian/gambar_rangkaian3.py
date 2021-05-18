# program gambarRangkaian3
    # menggambar template rangkaian 3 menggunakan schemdraw
# KAMUS
    # d : schemdraw.drawing
# ALGORITMA UTAMA
import schemdraw
import schemdraw.elements as elm
from math import sqrt
#schemdraw.use('svg')
def rangkaian3(R1,R2,R3,R4,V1):
        # menginisiasi rangkaian
    d = schemdraw.Drawing()

        # menambahkan elemen pada rangkaian
    d += elm.Dot().label('a',loc = 'top')
    d += elm.Line().left().length(1)

    d += elm.Resistor().theta(60).label(R1,loc   ="top")
    d += elm.Line().left()
    d += elm.SourceV().down().reverse().length(3*sqrt(3)).label(V1)
    d += elm.Line().right()
    d.push()

    d += elm.Resistor().theta(120).label(R3,loc   ="bottom")

    d.pop()
    d += elm.Resistor().theta(60).label(R4,loc   ="bottom")
    d.push()

    d += elm.Resistor().theta(120).label(R2,loc   ="top")

    d.pop()
    d += elm.Line().left().length(1)
    d += elm.Dot().label('b',loc = 'top')

        # menggambar rangkaian yang telah disusun
    d.draw()
