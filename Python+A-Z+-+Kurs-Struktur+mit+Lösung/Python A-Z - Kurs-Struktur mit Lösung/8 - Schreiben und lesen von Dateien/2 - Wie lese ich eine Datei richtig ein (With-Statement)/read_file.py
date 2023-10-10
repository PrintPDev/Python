'''

Mit Python ist es super einfach auch Inhalt einer Datei einzulesen und 
auch Inhalt in einer Datei zu schreiben. 

Wir mussten bisher immer eine Verbindung öffnen und schließen. 
Lass uns jetzt mal schauen wie wir automatisch die Datei wieder schließen können.

'''

def main():
    fopen = open('autos.txt', 'r')

    erste_zeile = fopen.readline()
    print('Erste Zeile: ', erste_zeile)

    alle_zeilen = fopen.readlines()
    print('Alle Zeilen: ', alle_zeilen)
    print('Type ? ', type(alle_zeilen))

    for zeile in alle_zeilen:
        #print(zeile)
        # entferne leerzeichen rechts
        zeile = zeile.rstrip()
        elemente = zeile.split(',')
        #print(elemente)

        # Jetzt kann ich auf den Namen zugreifen
        name_anzeige = elemente[0]
        print('Anzeige: ', name_anzeige)

    # Verbindung zur Datei schließen
    fopen.close()


if __name__ == "__main__":
    main()