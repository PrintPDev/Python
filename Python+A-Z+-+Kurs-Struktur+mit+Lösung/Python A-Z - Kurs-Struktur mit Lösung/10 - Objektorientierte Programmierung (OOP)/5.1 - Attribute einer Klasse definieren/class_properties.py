'''
Fortsetzung: 

Sobald eine Klasse erstellt werden muss, ist die komplexität so "stark", dass die 
Klasse auch mit Attribute (Eigenschaften) ausgestattet werden muss.

Beispiel: Die Klasse Person hat als Attribute: Name und Alter

'''

class Person: 
    pass


def main():
    p1 = Person()
    p1.name = 'Saif'
    print('p1: ', p1.__dict__)

    p2 = Person()
    p2.name = 'Jan'
    print('p2: ', p2.__dict__)

    Person.alter = 27
    print('p1: ', p1.__dict__) # Attribut "Alter" nicht vorhanden, vielleicht in Person?
    print('Person: ', Person.__dict__) # Jetzt Ja! 
    
    # Aber ist es nun auch in den Objekten, trotz des fehlen im p1/2.__dict__?
    print('Alter von p1 ist: ', p1.alter)
    print('Alter von p2 ist: ', p2.alter)
    
    '''
    Daraus folgt: Python sucht nach Attributen zuerst im Objekt (p1 / p2) und dann in der Klasse
    '''

    # Was ist wenn wir ein Attribut ausgeben, dass nicht existiert?
    print('Nachname von p1: ', p1.nachname) # Wirft ein AttributeError!



if __name__ == "__main__":
    main()
