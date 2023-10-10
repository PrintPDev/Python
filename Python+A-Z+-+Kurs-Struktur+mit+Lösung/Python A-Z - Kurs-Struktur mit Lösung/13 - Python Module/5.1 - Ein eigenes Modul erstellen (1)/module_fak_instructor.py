'''
Lass uns nun unser eigenes Modul erstellen! Hierfür wollen wir unsere Fakultaet 
Funktionen auslagern in ein eigenes Modul, dass "fakultaet" heißt!


'''
# Schritt 1: importieren von fakultaet
import fakultaet
# Schritt 2: importiere nur die rekursive Funktion 
from fakultaet import recursive_fakultaet

def main():
    f_5 = fakultaet.recursive_fakultaet(5)
    print('Ergebnis: ', f_5)
    f_5 = fakultaet.iterative_fakultaet(5)
    print('Ergebnis: ', f_5)

if __name__ == "__main__":
    main()