# program gambarRangkaian1
    # menggambar template rangkaian 1 menggunakan schemdraw
# KAMUS
    # d : schemdraw.drawing
# ALGORITMA UTAMA
import schemdraw
import schemdraw.elements as elm
schemdraw.use('svg')

    # menginisiasi rangkaian
d = schemdraw.Drawing()

    # menambahkan elemen pada rangkaian
d += elm.Dot().label('a',loc = 'right')
d += elm.Resistor().left().label("R1",loc="bottom")
d.push()

d += elm.Resistor().left().label("R2",loc="bottom")
d += elm.SourceV().down().reverse().label("V1")
d += elm.Line().right()

d.pop()
d += elm.Resistor().down().label("R3",loc="bottom")
d += elm.Line().right()
d += elm.Dot().label('b',loc = 'right')

    # menggambar rangkaian yang telah disusun
d.draw()
