'''

Sobald eine Klasse erstellt werden muss, ist die komplexität so "stark", dass die 
Klasse auch mit Attribute (Eigenschaften) ausgestattet werden muss.

Beispiel: Die Klasse Person hat als Attribute: Name und Alter

'''

class Person: 
    pass


def main():
    p1 = Person()
    
    p1.name = 'Saif'
    p1.alter = 27

    print('Daten von p1: ', p1.name, p1.alter)

    p2 = Person()
    
    p2.name = 'Jan'
    p2.alter =  25
    
    print('Daten von p2: ', p2.name, p2.alter)



if __name__ == "__main__":
    main()
