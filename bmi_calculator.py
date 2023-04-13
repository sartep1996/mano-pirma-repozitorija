svoris = float(input("Sveiki, įveskite savo svorį kg : "))
ūgis = float(input("Sveiki, įveskite savo ūgį cm : ")) / 100
vardas = str(input("Įveskite savo vardą: "))
vardas_c = vardas.capitalize()
vardas_c = vardas_c.capitalize()

kūnoMasėsIndeksas = svoris / (ūgis**2)
tekstas = f"Jūsų svoris yra {svoris}kg ir jūsų ūgis yra {ūgis}m \
kūno masės indeksas: " + str(kūnoMasėsIndeksas)
print(tekstas)

if kūnoMasėsIndeksas <= 18.5:
    print(vardas_c + " jūsų svoris yra per mažas")
elif kūnoMasėsIndeksas <= 25:
    print(vardas_c + " jūsų svoris yra normalus")
elif kūnoMasėsIndeksas <= 30:
    print(vardas_c + " jūs esate nutukęs")
else: print(vardas_c + " jūs esate laaaaabaiiiii nutukęs")

