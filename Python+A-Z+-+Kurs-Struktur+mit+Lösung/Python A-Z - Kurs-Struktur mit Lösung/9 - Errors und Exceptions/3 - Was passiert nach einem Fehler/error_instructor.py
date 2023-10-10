'''

Wir haben nun gesehen wie wir (mehrere) Fehler abfangen können. 
Allerdings müsste man öfters nachdem die Fehlerbehandlung durchgeführt wurde
auch abschließende Aktionen durchführen.

Wie können wir so etwas durchführen? Lass uns einen Fall durchgehen!

'''


def main():
    try:
        x = input('Gebe eine Zahl ein')
        x = float(x)
        r = 1.0 / x
    except ValueError:
        print('Bitte gebe entweder ein int oder float ein')
    except ZeroDivisionError:
        print('Ein Fehler ist aufgetreten')
    finally:
        print('Programm 2 angestoßen')

if __name__ == "__main__":
    main()