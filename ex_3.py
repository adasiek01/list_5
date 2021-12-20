from turtle import *

from turtle import *

def hilbert(number, ang, length):
    """Argumenty(3): number - rząd krzywej, agle - kąt krzywej, length - rozmiar jednego kroku
    Funkcja rysuje krzywą Hilberta rekurencyjnie. Zwraca błąd jeśli number nie jest liczbą całkowitą lub jest mniejsze od zera."""
    if number < 0 or not (float(number)).is_integer():  # is_integer() works for float types, for e.g. 1.0.is_integer() == True
        raise IndexError("Variable n should be an integer higher than 0.")
    
    

    if number == 0:
        return

    # turn right
    right(ang)
    hilbert(number-1, - ang, length)
    dot(8,"pink")

    # length and turn left
    forward(length)
    left(ang)
    hilbert(number-1, ang, length)
    dot(12,"yellow")

    forward(length)
    hilbert(number-1, ang, length)
    dot(14,"blue")

    left(ang)
    forward(length)
    hilbert(number-1, -ang, length)

    right(ang)


def draw(number):
    """Argumenty(1): number - rząd krzywej
    Funkcja rysuje krzywą Hilberta rekurencyjnie z wykorzystaniem powyższej funkcji hilbert. 
    Przekazuje do niej rozmiar, pozycję początkową żółwia oraz kąt na 90 stopni."""
    size = 200
    penup()
    goto(-size // 2, size // 2)
    pendown()
    hilbert(number, 90, size//(2*number+1))       
    done()

if __name__ == "__main__":
    draw(4)



if __name__ == "__main__":
    print(hilb())
