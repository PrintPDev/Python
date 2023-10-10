'''

Mithilfe von Modifikations-Richtlinien kann versichert werden, dass Attribute 
kontrolliert und restriktiert werden können. 

Es gibt drei Modifikatoren: public, protected und private

Public: Public-Attribute sind öffentlich und können von innerhalb der Klasse, 
außerhalb, sowie von anderen Klassen erreicht werden.

'''

class Person:
    name = None
    alter = None

    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def daten_ausgeben(self):
        print('Mein Name ist: ', self.name)
        print('Mein Alter ist: ', self.alter)

    def daten_aendern(self, name, alter):
        self.name = name
        self.alter = alter


def main():
    p1 = Person('Saif', 27)
    p1.daten_ausgeben()
    p1.daten_aendern('Jan', 25)
    p1.daten_ausgeben()


if __name__ == "__main__":
    main()
