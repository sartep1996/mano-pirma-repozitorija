svoris = float(input("Sveiki, įveskite savo svorį kg : "))
ūgis = float(input("Sveiki, 5veskite savo ūgį cm : "))/100
print("Įveskite savo ūgį")

kūnoMasėsIndeksas = svoris / (ūgis**2)
tekstas = f"Jūsų svoris yra {svoris} ir jūsų ūgis yra {ūgis} \
      kūno masės indeksas: " + str(kūnoMasėsIndeksas)
print(tekstas)

if kūnoMasėsIndeksas <= 18.5:
    print("Svoris per mažas")
elif kūnoMasėsIndeksas <= 25:
    print ("Jūsų svoris normalus")
elif kūnoMasėsIndeksas <= 30:
    print("Jūs esate nutukęs")
else: print("jūs esate labaiiiii nutukęs")

