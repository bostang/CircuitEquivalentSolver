# program gambarRangkaian5
    # menggambar template rangkaian 5 menggunakan schemdraw
# KAMUS
    # d : schemdraw.drawing
# ALGORITMA UTAMA
import schemdraw
import schemdraw.elements as elm
#schemdraw.use('svg')
def rangkaian5():
        # menginisiasi rangkaian
    d = schemdraw.Drawing()

        # menambahkan elemen pada rangkaian
    d += elm.Dot().label('a',loc = 'top')
    d += elm.Line().left().length(1)
    d += elm.Resistor().left().label("R5",loc   ="top")
    d += elm.Resistor().left().label("R1",loc   ="top")
    d += elm.SourceV().down().reverse().label("V1")
    d += elm.Resistor().label("R2",loc   ="top")
    d += elm.Line().right()
    d += elm.Resistor().up().label("R4",loc   ="top")
    d.push()

    d += elm.Resistor().up().label("R3",loc   ="top")

    d.pop()
    d += elm.Line().right().length(4)
    d += elm.Dot().label('b',loc = 'top')

        # menggambar rangkaian yang telah disusun
    d.draw()
