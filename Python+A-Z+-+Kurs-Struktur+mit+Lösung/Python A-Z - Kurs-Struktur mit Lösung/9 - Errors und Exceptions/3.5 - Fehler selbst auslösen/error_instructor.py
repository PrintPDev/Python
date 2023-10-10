'''

Wir haben nun gesehen wie wir (mehrere) Fehler abfangen können. 
Allerdings müsste man öfters auch selbst Fehler auslösen, damit
keine Fehlerhaften Eingaben getätigt werden können!

'''

def f(x):
    if type(x) != float:
        raise TypeError('x muss ein Int oder Float sein!')
    print('Die Zahl ist: ', x)

def main():
    x = input('Gebe eine Zahl ein')
    # x = float(x)
    f(x)

if __name__ == "__main__":
    main()