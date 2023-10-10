'''

Mit Python ist es super einfach auch Inhalt einer Datei einzulesen und 
auch Inhalt in einer Datei zu schreiben. 

Lass uns jetzt mal schauen wie wir in einer Datei schreiben können.

'''

def main():
    with open('autos.txt', 'r') as fread:
        zeilen = fread.readlines()
        
        with open('anzeigen.txt', 'w') as fwrite:
            for zeile in zeilen:
                attr = zeile.split(',')
                anzeige_name = attr[0]
                # hier die neue datei zu öffnen ist falsch, da schleife!
                fwrite.write(anzeige_name + '\n') # \n da sonst alles in eine Zeile


if __name__ == "__main__":
    main()