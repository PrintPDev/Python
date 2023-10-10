'''
Jedes Python-Modul ist über den Namen des Moduls ansprechbar. Es ist jedoch so,
dass abhängig wie häufig du das Modul aufrufst es nervig sein kann den vollen Namen
des Moduls aufzurufen.


'''

# Schritt 1: importieren von math als m
import math as m
# Schritt 2: importieren der Funktion sin und cos von math
from math import sin as sinus, pow as potenz


def main():
    # Schritt 1
    s = m.sin(4)
    print('Sinus von 4: ', s)
    p = m.pow(2, 4)
    print('Potenz von 4: ', p)

    # Schritt 2
    s = sinus(3)
    print('Sinus von 3: ', s)
    p = potenz(2, 3)
    print('Potenz von 3: ', p)

if __name__ == "__main__":
    main()