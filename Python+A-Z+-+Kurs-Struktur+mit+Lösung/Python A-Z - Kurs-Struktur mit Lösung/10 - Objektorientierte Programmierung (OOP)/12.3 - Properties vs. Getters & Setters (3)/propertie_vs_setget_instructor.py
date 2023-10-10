'''

In der letzten Lektion haben wir Datenkapslung anhand von setter und getter "Schnittstellen"
umgesetzt. Allerdings ist das nicht der Pythonic-Way so etwas zu implementieren. 

Komischerweise ist es in Python üblich Attribute öffentlich zu setzen und Datenkapslung
über ein Decorater zu realisieren.

Wie? 

-> Wir erstellen Funktion worüber Python weiß, dass diese für das schreiben und lesen eines Attributes ist.


'''

class Person:
    alter = 0

    def __init__(self, alter):
        self.alter = alter

    def daten_ausgeben(self):
        print('Mein Alter ist: ', self.__alter)
    
    @property
    def alter(self):
        return self.__alter
    
    @alter.setter
    def alter(self, alter):
        if alter < 0:
            raise ValueError('Das Alter darf nicht kleiner sein als 0!')
        else:
            self.__alter = alter


def main():
    p1 = Person(27) # auch hier greift unsere setter Funktion!
    p1.daten_ausgeben()
    p1.alter = 13
    print(p1.__dict__)
    #p1.alter = -5 # wirft unser ValueError


if __name__ == "__main__":
    main()
