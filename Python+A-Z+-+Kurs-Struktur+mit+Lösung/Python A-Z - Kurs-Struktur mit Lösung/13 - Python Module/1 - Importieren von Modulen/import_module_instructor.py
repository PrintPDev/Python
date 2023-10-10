'''
Wie bereits erwähnt gibt es in Python sehr viele eingebaute Module! Ein sehr rudimentäres Modul ist
die Standard-Bibliothek für Mathematischeoperationen. 

Lass uns diese importieren!

'''

# Schritt 1: importieren von math
import math
# Schritt 2: importieren der Funktion sin und cos von math
from math import sin, cos
# Schritt 3: importieren von math und random
import math, random


def main():
    # Schritt 1
    s = math.sin(4)
    print('Sinus von 4: ', s)
    c = math.cos(4)
    print('Cosinus von 4: ', c)

    # Schritt 2
    s = sin(3)
    print('Sinus von 3: ', s)
    c = cos(3)
    print('Cosinus von 3: ', c)

    # Schritt 3
    n = random.randint(1, 10)
    print('Zufällige Zahl zwischen 1 und 10: ', n)

if __name__ == "__main__":
    main()