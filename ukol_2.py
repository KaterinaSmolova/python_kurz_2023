sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod_soucastky = str(input("Zadej kód součástky: "))

if kod_soucastky in sklad:
   mnozstvi = int(input("Zadej počet kusů: ")) 
else:
    print(f"Součástka není skladem")

sklad[kod_soucastky] -= mnozstvi

print (sklad) # nemusí tu být

if sklad[kod_soucastky] < 1:
    print(f"Lze prodat pouze omezené množství kusů!")
    del sklad[kod_soucastky]
else: 
    print(f"Poptávku lze uspokojit v plné výši!")

print (sklad) # nemusí tu být 