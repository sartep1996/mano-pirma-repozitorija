
def ar_pirminis(n):
    if n < 2:
        return False
    for number in range(2,n):
        if n % number == 0:
            return False
    return True

def pirminiai_skaiciai_iki_n (skaicius):
    for n in range(2, skaicius):
        if ar_pirminis(n):
            yield n

pirminiai_generatorius = pirminiai_skaiciai_iki_n(1000000)

for skaicius in pirminiai_generatorius:
    print (skaicius)
