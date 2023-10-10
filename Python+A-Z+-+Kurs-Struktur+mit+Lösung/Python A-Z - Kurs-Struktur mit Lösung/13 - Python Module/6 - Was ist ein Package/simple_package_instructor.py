'''
Wir haben gelernt, dass Module Dateien sind, die Python-Anweisungen und Definitionen enthalten, 
wie Funktions- und Klassendefinitionen. Wir werden in diesem Abschnitt lernen, 
wie man mehrere Module zu einem Paket zusammenfasst.

Ein Paket ist im Grunde ein Verzeichnis mit Python-Dateien und eine Datei mit dem Namen __init__.py. 
Das bedeutet, dass jedes Verzeichnis innerhalb des Python-Pfades, das eine Datei mit dem Namen __init__.py 
enthält, von Python als Paket behandelt wird. Es ist möglich, mehrere Module in ein Paket zu packen.

Pakete sind eine Möglichkeit, den Modulnamensraum von Python durch die Verwendung von "gepunkteten Modulnamen" zu strukturieren. 
A.B steht für ein Untermodul mit dem Namen B in einem Paket mit dem Namen A. 
Zwei verschiedene Pakete wie P1 und P2 können beide Module mit dem gleichen Namen haben, sagen wir zum Beispiel A. 
Das Untermodul A des Pakets P1 und das Untermodul A des Pakets P2 können völlig unterschiedlich sein.
Ein Paket wird wie ein "normales" Modul importiert.

'''



def main():
    print(test_package)

if __name__ == "__main__":
    main()