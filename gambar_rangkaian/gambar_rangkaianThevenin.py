# Program TheveninEquivalent
    # menggambar rangkaian ekuivalen thevenin dari rangkaian utama
# KAMUS
    # Variabel
        # R_in : integer { nilai resistansi input }
        # V_in : integer { nilai sumber tegangan input }
    # Fungsi / Prosedur
        # procedure Thevenin_draw(input  V_th, R_th : integer)
            # menggambar rangkaian ekuivalen thevenin dari 2 buah titik

# ALGORITMA UTAMA
import schemdraw
import schemdraw.elements as elm

def rangkaianThevenin(V_th,R_th):
    d = schemdraw.Drawing()
    d += elm.Dot().label('b',loc = 'top')
    d += elm.Line().left().label("")
    d += elm.SourceV().up().label(f"V_th = {V_th} V")
    d += elm.Resistor().label(f"R_th = {R_th} Ohm")
    d += elm.Line().right().label("")
    d += elm.Dot().label('a',loc = 'bottom')
    d.draw()
