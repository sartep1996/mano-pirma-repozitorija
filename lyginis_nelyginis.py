digit = float(input("Sveiki, įveskite savo skaičių: "))

digit2 = digit + (digit**3)

if digit2 % 2 == 0:
    print("Jūsų skaičius " + str(digit2) + " yra lyginis")
else: print("Jūsų skaičius " + str(digit2) + "yra ne lyginis")