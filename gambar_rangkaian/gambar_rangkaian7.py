# program gambarRangkaian7
    # menggambar template rangkaian 7 menggunakan schemdraw
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
d += elm.Line().left().length(1)
d.push()
d += elm.Resistor().left().label("R3",loc   ="top")
d += elm.SourceV().down().reverse().label("V3")
d.pop()

d += elm.Line().up().length(1)

d.push()
d += elm.Resistor().left().label("R2",loc   ="top")
d += elm.Line().left().length(2)
d += elm.Line().down().length(1)
d += elm.SourceV().down().reverse().label("V2")
d.pop()

d += elm.Line().up().length(1)
d += elm.Resistor().left().label("R1",loc   ="top")
d += elm.Line().left().length(4)
d += elm.Line().down().length(2)
d += elm.SourceV().down().reverse().label("V1")

d += elm.Line().right().length(8)
d += elm.Dot().label('b',loc = 'top')


    # menggambar rangkaian yang telah disusun
d.draw()