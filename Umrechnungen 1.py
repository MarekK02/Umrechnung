# kpa in bar umrechnung
def KPA_in_Bar(kpa):
    bar = kpa * 100
    return bar


# bar in kpa umrechnung
def Bar_in_KPA(bar):
    kpa = bar / 100
    return kpa  # Das was die Funktion dir zurückgibt (return)


# celsius in fahrenheit
def Celsius_in_Fahrenheit(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

# fahrenheit in celsius
def Fahrenheit_in_Celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# kw in ps
def KW_in_PS(kw):
    ps = (kw * 1.63)
    return ps

# ps in kw
def PS_in_KW(ps):
    kw = (ps * 0.74)
    return kw

# feet in cm
def Feet_in_Cm(feet):
    cm = (feet * 30.48)
    return cm

#cm in feet
def Cm_in_Feet(cm):
    feet = (cm / 30.48)
    return feet

# zoll in cm
def Zoll_in_Cm(zoll):
    cm = (zoll * 2.54)
    return cm

# cm in zoll
def Cm_in_Zoll(cm):
    zoll = (cm / 2.54)
    return zoll

# Auswahl der Umrechnungen
print("Gebe bitte:")
print("(1) für die Berechnung von KPA in Bar ein")
print("(2) für die Berechnung von Bar in KPA ein")
print("(3) für die Berechnung von Celsius in Fahrenheit ein")
print("(4) für die Berechnung von Fahrenheit in Celsius ein")
print("(5) für die Berechnung von KW in PS ein")
print("(6) für die Berechnung von PS in KW ein")
print("(7) für die Berechnung von Feet in CM ein")
print("(8) für die Berechnung von CM in Feet ein")
print("(9) für die Berechnung von Zoll in CM ein")
print("(10) für die Berechnung von CM in Zoll ein")

eingabe = int(input("Eingabe: "))  # Der User bestimmt hier welche Rechenoperation er auswählen möchte


def Funktionsparameter():  # Funktion, die die Variable 'x' in die jeweilige Funktion einsetzt
    x = float(input("Deine Zahl: "))
    return x


match eingabe:  # Switch-Case
    case 1:
        print(KPA_in_Bar(Funktionsparameter()))
    case 2:
        print(Bar_in_KPA(Funktionsparameter()))
    case 3:
        print(Celsius_in_Fahrenheit(Funktionsparameter()))
    case 4:
        print(Fahrenheit_in_Celsius(Funktionsparameter()))
    case 5:
        print(KW_in_PS(Funktionsparameter()))
    case 6:
        print(PS_in_KW(Funktionsparameter()))
    case 7:
        print(Feet_in_Cm(Funktionsparameter()))
    case 8:
        print(Cm_in_Feet(Funktionsparameter()))
    case 9:
        print(Zoll_in_Cm(Funktionsparameter()))
    case 10:
        print(Cm_in_Zoll(Funktionsparameter()))
    case _:
        print("Eingabe der Zahl unbekannt")