skaicius1 = float(input("Sveiki, įveskite pirmą skaičių: "))
skaicius2 = float(input("Iveskite antrą skaičių: "))

galutinisSkaicius = skaicius1*skaicius2*100/(skaicius1-skaicius2)

tekstas = f"Suformatuoutas galutinis skaicius yra: {galutinisSkaicius:.2f}"
print(tekstas)

