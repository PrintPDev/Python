'''
Fortsetzung: 

Sobald eine Klasse erstellt werden muss, ist die komplexität so "stark", dass die 
Klasse auch mit Attribute (Eigenschaften) ausgestattet werden muss.

Beispiel: Die Klasse Person hat als Attribute: Name und Alter

'''

class Person: 
    name = None
    alter = None


def main():
    p1 = Person()
    p1.name = 'Saif'
    p1.alter = 27
    print(p1.name, p1.alter)


if __name__ == "__main__":
    main()
