'''

Mithilfe von Modifikations-Richtlinien kann versichert werden, dass Attribute 
kontrolliert und restriktiert werden können. 

Es gibt drei Modifikatoren: public, protected und private

Protected: Protected-Attribute können nur innerhalb der Klasse
und von geerbten Klassen ereicht werden.

'''

class Person:
    _name = None
    _alter = None

    def __init__(self, name, alter):
        self._name = name
        self._alter = alter

    def daten_ausgeben(self):
        print('Mein Name ist: ', self._name)
        print('Mein Alter ist: ', self._alter)

    def daten_aendern(self, name, alter):
        self._name = name
        self._alter = alter


def main():
    p1 = Person('Saif', 27)
    p1._name = 'Saif'
    p1._alter = 27
    p1.daten_ausgeben()
    p1.daten_aendern('Jan', 25)
    p1.daten_ausgeben()


if __name__ == "__main__":
    main()
