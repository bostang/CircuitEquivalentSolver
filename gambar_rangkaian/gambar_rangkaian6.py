# program gambarRangkaian6
    # menggambar template rangkaian 6 menggunakan schemdraw
# KAMUS
    # d : schemdraw.drawing
# ALGORITMA UTAMA
import schemdraw
import schemdraw.elements as elm
schemdraw.use('svg')

    # menginisiasi rangkaian
d = schemdraw.Drawing()

    # menambahkan elemen pada rangkaian
d += elm.Dot().label('a',loc = 'top')
d += elm.Resistor().left().label("Rf",loc   ="top")

d.push()
d += elm.Line().up()
d += elm.Resistor().left().label("R1",loc   ="top")
d += elm.SourceV().left().reverse().label("V1")
d += elm.Line().down()
d.pop()

d.push()
d += elm.Line().down()
d += elm.Resistor().left().label("R3",loc   ="top")
d += elm.SourceV().left().reverse().label("V3")
d += elm.Line().up()
d.pop()

d += elm.Resistor().left().label("R2",loc   ="top")
d += elm.SourceV().left().reverse().label("V2")

d += elm.Resistor().left().label("Ri",loc   ="top")
d += elm.Dot().label('b',loc = 'top')

    # menggambar rangkaian yang telah disusun
d.draw()
