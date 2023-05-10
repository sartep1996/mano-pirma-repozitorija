import sqlite3
conn = sqlite3.connect("mano-pirma-repozitorija/masinos_uzduotis/automobiliai.db")
c = conn.cursor()

while True:
    print("""===[Masinu Katalogas]===
    1 - Paieska pagal MARKE
    2 - Paieska pagal MODELI
    3 - Paieska pagal SPALVA
    4 - Paieska pagal METUS
    5 - Paieska pagal KAINA
    """)
    choice = input("Pasirinkite: ")
    if choice == "1":
        marke = input("Marke: ")
        with conn:
            c.execute('Select rowid, * FROM masina WHERE marke =?', (marke, ))
            masina = c.fetchall()

        if masina and len(masina) > 0:
            for masin in masina:
                print(masin)

        
   
    elif choice == "2":
        modelis = input("Modelis: ")
        with conn:
            c.execute('Select rowid * FROM masina WHERE modelis =?',(modelis, ))
            modelis = c.fetchall()

        if masina and len(masina) > 0:
            for masin in masina:
                print(masin)

    elif choice == "3":
        spalva = input("Spalva: ")
        with conn:
            c.execute('Select rowid * FROM masina WHERE spalva =?',(spalva, ))
            modelis = c.fetchall()

    elif choice == "4":
        metai = input("Metai: ")
        with conn:
            c.execute('Select rowid * FROM masina WHERE metai =?',(metai, ))
            metai = c.fetchall()

    elif choice == "5":
        kaina = kaina("Kaina: ")
        with conn:
            c.execute('Select rowid * FROM masina WHERE kaina =?', (kaina,))

    else:
        break

c.close


