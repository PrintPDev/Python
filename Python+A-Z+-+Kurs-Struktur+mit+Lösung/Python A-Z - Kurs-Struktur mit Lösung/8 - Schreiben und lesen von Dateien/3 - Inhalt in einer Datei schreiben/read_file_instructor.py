'''

Mit Python ist es super einfach auch Inhalt einer Datei einzulesen und 
auch Inhalt in einer Datei zu schreiben. 

Lass uns jetzt mal schauen wie wir in einer Datei schreiben können.

'''

def main():
    with open('anzeigen.txt', 'w') as f:
        f.write('Benz CLA45\n')
        f.write('Ford Raptor\n')
        f.write('Audi Q8\n')


if __name__ == "__main__":
    main()