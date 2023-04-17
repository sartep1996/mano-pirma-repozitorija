atlyginimas = 1600

print("Jusu atlyginimas: " + str(atlyginimas))

perdiena = float(input("Kiek išleidžiate per dieną: "))


dienos = 0

# while atlyginimas > 0:
#     atlyginimas = atlyginimas - perdiena
#     dienos = dienos + 1

    
# print("Reikės", dienos, "kad išleistumėte visą atlyginimą" )


for dienos in range(1,1000000000000000):
    atlyginimas = atlyginimas - perdiena
    if atlyginimas > 0:
        print ("Prireike", dienos, "kad isleisti visa atlyginima")
