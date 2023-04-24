
import json

with open('python_kurz_2023/body.json', encoding='utf-8') as file: 
    vysledky = json.load(file)

for klic, hodnota in vysledky.items():
    if hodnota > 60:
      vysledky [klic] = "PASS"
    else: 
        vysledky [klic] = "FAIL"

print(vysledky)

with open('output.json', mode='w', encoding='utf-8') as file:
    json.dump(vysledky, file)
   
