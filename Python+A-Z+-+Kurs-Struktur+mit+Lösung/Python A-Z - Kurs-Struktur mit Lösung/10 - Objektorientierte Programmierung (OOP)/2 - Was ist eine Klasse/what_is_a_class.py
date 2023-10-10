'''

In dieser Lektion schauen wir uns das Element "Klasse" an. 
Insbesondere werden wir sehen was alles in Python eine Klasse ist. 

Tipp: Alles ist eine Klasse in Python!

'''

# Das kennen wir bereit: type von int
x = 42
print(type(x))

# Was ist mit Float? Da ist es ja das selbe. 
y = 4.67
print(type(y))

# Was ist mit einer Funktion?
def f(x):
    return x + x

print(type(f))

# Wie ist es mit einer Datenstruktur?

a = [5, 6, 7]
a.append(8) # Hier ist die Funktion ein bestandteil der Klasse List
print(type(a))

