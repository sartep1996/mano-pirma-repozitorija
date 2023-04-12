konversijos_tipas = input("Pasirinkite konversijos tipą (įveskite C arba F): ")
temperatura = input("Įveskite temperatūrą: ")

if konversijos_tipas == "C":
    fahrenheit = float(temperatura) * 9/5 + 32
    print(f"{temperatura} laipsnių Celsijaus yra {fahrenheit:.2f} laipsnių Farenheito.")
elif konversijos_tipas == "F":
    celsius = (float(temperatura) - 32) * 5/9
    print(f"{temperatura} laipsnių Farenheito yra {celsius:.2f} laipsnių Celsijaus.")
else:
    print("Neteisingas konversijos tipas. Bandykite dar kartą.")
    