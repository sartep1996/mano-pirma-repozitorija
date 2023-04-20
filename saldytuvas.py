import os

saldytuvas = {"mesa":1}

def pridėti_produktą (pavadinimas, kiekis):
    global saldytuvas
    if pavadinimas in saldytuvas:
        saldytuvas[pavadinimas] += kiekis
    else:
        saldytuvas[pavadinimas] = kiekis

os.system('clear')
print ("labas pasirinkite ka norite padaryti?")
print("1 - perziureti saldytuva", "2 - prideti produka", "3 - issimti produkta", "4 - suskaiciuoti turinio svori", "9 - iseiti" )
user_input = int(input("Irasykite savo pasirinkima: "))

while True:
    user_input != 1 or 2 or 3 or 4
    break

if user_input == 1:
    os.system('cls')
    print(saldytuvas)
if user_input == 2:
    print(pridėti_produktą(pavadinimas,))
















if user_input == 3:
    os.system('cls')
    print(user_input)
if user_input == 4:
    os.system('cls')
    print(user_input)
# if user_input != 1 or 2 or 3 or 4:  
#     break