'''

Nachdem wir gesehen haben wie einfach es ist eine Klasse zu erstellen, 
müssen wir nun klären, woran man ein "Objekt" erkennt.

Tipp: Bei jeder zuweisung einer Klasse ensteht ein Objekt dieser Klasse!

'''

class Person: 
    pass


def main():
    p1 = Person() # neues Objekt 
    p2 = Person()

    p3 = p1

    print('Ist p3 = p1? ', (p3 == p1), id(p3), id(p1))
    print('Ist p1 = p2? ', (p1 == p2), id(p1), id(p2))

if __name__ == "__main__":
    main()
