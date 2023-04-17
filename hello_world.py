# skaicius = int(input("Įveskite skaiciu: "))

# if skaicius >= 0:
#     print("Skaicius yra teigiamas")
# else:
#     print("Skaicius yra neigiamas")




# skaicius = int(input("Įveskite skaiciu: "))

# if skaicius >= 5 and skaicius <= 10:
#     print("Skaicius yra teigiamas")
# elif skaicius <5 or skaicius > 10:
#     print("Skaicius yra neigiamas")




# skaicius = int(input("Įveskite skaiciu: "))
# skaicius2 = int(input("Įveskite skaiciu: "))

# if skaicius and skaicius2 >0:
#     print("Abu skaičiai yra didesni nei 0")
# else:
#     print("Bent vienas skaičius yra neigiamas arba lygus 0")





# skaicius = int(input("Įveskite skaiciu: "))
# skaicius2 = int(input("Įveskite skaiciu: "))   

# if skaicius % 2 == 0 and skaicius2 % 2 == 0:
#     print("skaicius yra lyginis")
# else:
#     print("bent vienas is skaiciu nera lyginis")



# 1.
# simboliuEilute = (input("Įveskite simboliu eilute: "))

# print(simboliuEilute[0], simboliuEilute[-1])




# 2.
# simboliuEilute = "Ziedu Valdovas"
# print(simboliuEilute[:5])


# 3. 
# simboliuEilute = "\"Gyveinmas yra trumpas\""
# print(simboliuEilute[-4:])

# # 4.
# simboliuEilute1 = (input("Įveskite simboliu eilute 1: "))
# simboliuEilute2 = (input("Įveskite simboliu eilute 2: "))

# print(simboliuEilute2[0] + "-" + simboliuEilute1[0] )



# 6.

# vardas = str(input("Sveiki, iveskite savo varda: "))
# amzius = int(input("Sveiki iveskite savo amziu: "))
# dabartiniaiMetai = 2023
# sueisSiaisMetais = 99 - int(amzius) + dabartiniaiMetai
# print("jusu vardas yra " + vardas + " ir jums sueis 100 metu " + str(sueisSiaisMetais ))


#7.

# jusuUgis = float(input("Sveiki, iveskite savo ugi centimetrais: "))
# jusuUgisMetrais = jusuUgis/100
# print("Jusu ugis centimetrais: " + str(jusuUgis))
# print("Jusu ugis metrais: " +  str(jusuUgisMetrais ))




#8.

# Atlyginimas = float(input("Iverskite savo atlyginima: "))
# atlyginimoMokestis = 20
# atlyginimasGalutinis = Atlyginimas - (1- atlyginimoMokestis/100)
# print("Jusu galutinis atlyginimas: " + str(atlyginimasGalutinis ))

#9.

# print("Sveiki Atvyke i laipsniu skaiciuotuva ")
# print("Pasirinkite konversija: ")
# print("1 - F to Cel")
# print("2 - Cel to F")

# choice = input("Iveskite savo pasirinkima ")
# temperatura = float(input("Iveskite savo laipsnius "))

# if choice == "1":
#     Cel = (float(temperatura) - 32) * 5/9
#     print(f"{temperatura} laipsnių Farenheito yra {Cel:.2f} laipsnių Celsijaus.")
# elif choice == "2":
#     F = float(temperatura) * 9/5 + 32
#     print(f"{temperatura} laipsnių Celsijaus yra {F:.2f} laipsnių Farenheito.")
# else:
#     print("Neteisingas konversijos tipas. Bandykite dar kart1ą.")





# input = str(input("Please enter your words: "))
# inputd = {}

# for i in input:
#     if i in inputd:
#         inputd[i] += 1
#     else:
#         inputd[i] =1
# print(inputd)



# numlist = [9, 2, 3, 4]
# min_num = numlist[0]

# for j in numlist:
#     if j <min_num:
#         min_num = j
# print(min_num)



list1 = [1, 2, 3, 4, 5]
currentbiggest = list1[0]

def biggest_number(list1):
    for number in list1:
        if number > currentbiggest:
            currentbiggest = number
    return currentbiggest

print(biggest_number(list1))