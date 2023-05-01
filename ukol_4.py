
def telefon (telefoni_cislo):
    if len(telefoni_cislo) == 9:
        return True
    elif len(telefoni_cislo) == 13 and (telefoni_cislo [:4]) == '+420':
        return True
    else:
        return False

telefoni_cislo = input("Zadej telefonní číslo, pro zaslání SMS: ")

print(telefon(telefoni_cislo))

import math

CENA = 3   
def cena_sms (pocet_znaku):
    sms = (math.ceil((len(pocet_znaku)) / 180)) * CENA
    return sms

pocet_znaku = input("Zadej text SMS: ")

print (f' Cena sms je:  {cena_sms(pocet_znaku)} Kč')
    
    



