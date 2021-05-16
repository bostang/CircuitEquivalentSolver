# program gambarRangkaian4
    # menggambar template rangkaian 4 menggunakan schemdraw
# KAMUS
    # d : schemdraw.drawing
# ALGORITMA UTAMA
import schemdraw
import schemdraw.elements as elm
#schemdraw.use('svg')
def rangkaian4():
        # menginisiasi rangkaian
    d = schemdraw.Drawing()

        # menambahkan elemen pada rangkaian
    d += elm.Dot().label('a',loc = 'top')
    d += elm.Line().left().length(2)
    d += elm.Resistor().left().label("R1",loc   ="top")
    d += elm.SourceV().down().length(6).label("V1")
    d += elm.Line().length(9).right()
    d += elm.SourceV().up().label("V3")
    d += elm.Resistor().label("R3",loc   ="top")
    d.push()

    d += elm.Line().up()
    d += elm.SourceV().left().label("V3")
    d += elm.Resistor().label("R2",loc   ="top")
    d += elm.Line().down()

    d.pop()
    d += elm.Line().left().length(2)
    d += elm.Dot().label('b',loc = 'top')

        # menggambar rangkaian yang telah disusun
    d.draw()
