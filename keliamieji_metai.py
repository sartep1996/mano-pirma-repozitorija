ivesti_metai = int(input("Sveiki, iveskite metus "))

for ivesti_metai in range(1900, 2100):
    if ivesti_metai % 4 == 0:
        print(str(ivesti_metai) + " yra keliamieji")
    else:
        print(str(ivesti_metai) + " nera keliamieji")


