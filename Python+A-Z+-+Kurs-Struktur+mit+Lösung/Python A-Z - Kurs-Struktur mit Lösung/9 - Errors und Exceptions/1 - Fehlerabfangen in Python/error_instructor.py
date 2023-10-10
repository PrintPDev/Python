'''

Kein Programm läuft immer reibungslos durch. Aus diesem Grund ist es essentiell 
Fehler zu erkennen und auch abzufangen. 

Wie? Das schauen wir uns jetzt an!

-> Szenario: Wir Fragen solange nach einem Int bis dieses eingegeben wurde.

'''


def main():

    while True:
        try:
            n = input('Bitte gebe eine ganze Zahl ein: ')
            n = int(n)
            print('Die Zahl ist: ', n)
            break
        except ValueError:
            print('Fehler! Bitte gebe eine ganze Zahl ein!')


if __name__ == "__main__":
    main()