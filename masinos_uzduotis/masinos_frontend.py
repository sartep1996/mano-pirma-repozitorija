import sqlite3
conn = sqlite3.connect("masinos_uzduotis/automobiliai.db")
c = conn.cursor()



while True:
    print("""===[Masinu Katalogas]===
    1 - Paieska pagal MARKE
    2 - Paieska pagal MODELI
    3 - Paieska pagal SPALVA
    4 - Paieska pagal METUS
    5 - Paieska pagal KAINA
    6 - IVESKITE AUTOMOBILI
    """)
    choice = input("Pasirinkite: ")
    
    if choice == "1":
        marke = input("Marke: ")
        with conn:
            c.execute('Select rowid, * FROM masina WHERE marke =?', (marke, ))
            masina = c.fetchall()
        if masina and len(masina) >0:
            for car in masina:
                print(masin)
   
    elif choice == "2":
        modelis = input("Modelis: ")
        with conn:
            c.execute('Select rowid, * FROM masina WHERE modelis =?',(modelis, ))
            modelis = c.fetchall()

        if modelis and len(modelis) > 0:
            for masin in modelis:
                print(masin)

    elif choice == "3":
        spalva = input("Spalva: ")
        with conn:
            c.execute('Select rowid, * FROM masina WHERE spalva =?',(spalva, ))
            spalva = c.fetchall()

        if spalva and len(spalva) > 0:
            for masin in spalva:
                print(masin)

    elif choice == "4":
        metai_nuo = input("Metai_nuo: ")
        metai_iki = input("Metai_iki: ")
        with conn:
            c.execute('SELECT rowid, * FROM masina WHERE pagaminimo_metai BETWEEN ? AND ?',(metai_nuo, metai_iki ))
            metai = c.fetchall()
        
        if metai and len(metai) > 0:
            for masin in metai:
                print(masin)


    elif choice == "5":
        kaina_nuo = input("Kaina_nuo: ")
        kaina_iki = input("Kaina_iki: ")
        with conn:
            c.execute('SELECT rowid, * FROM masina WHERE kaina BETWEEN ? AND ?', (kaina_nuo, kaina_iki))
            kaina = c.fetchall()
        
        if kaina and len(kaina) > 0:
            for masin in kaina:
                print(masin)

    elif choice == "6":
        marke = input("Iveskite marke: ")
        modelis = input("Iveskite modeli: ")
        spalva = input("Iveskite spalva: ")
        metai = input(int("Iveskite metai: "))
        kaina = input(int("Iveskite kaina: "))
        print (f'Automobilis: {marke}, {modelis}, {spalva}, {metai}, {kaina} ivestas')

        with conn:
            c.execute(''' INSERT INTO masina
(marke, modelis, spalva, pagaminimo_metai, kaina)
VALUES (?, ?, ?, ?)''',(marke, modelis, spalva, metai, kaina))
    else:
        break

c.close


