# try:
#     num1 = int(input("Iveskite pirma skaicius: "))
#     num2 = int(input("Iveskite antra skaiciu: "))
#     result = num1/ num2
# except ZeroDivisionError:
#     print("Negalima dalinti iš nulio!")
# except ValueError:
#     print("netinkamas skaiciaus formatas")
# finally:
#     print("Rezultatas: ",result)


def issaukimas(skaicius):
    if not isinstance(skaicius, (int, float)):
        raise ValueError("Funkcija veikia tik su sveikais skaiciais")
    return skaicius

input = input("Please enter number: ")
try: 
    num = issaukimas(float(input))
    print(num)
except ValueError as e:
    print(e)



# while True:
#     try:
#         skaicius = float(input("Įveskite teigiamą skaičių: "))
#         if skaicius < 0:
#             raise ValueError("Įvestas skaičius yra neigiamas")
#         else:
#             print("Ačiū, jūs įvedėte:", skaicius)
#             break
#     except ValueError as error:
#         print("Klaida:", error)

