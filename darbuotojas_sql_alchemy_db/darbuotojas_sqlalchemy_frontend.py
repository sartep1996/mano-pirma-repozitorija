from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from darbuotojas_sqlachemy_backend import Darbuotojas
from datetime import datetime


engine = create_engine('sqlite:///darbuotojas_sql_alchemy_db/darbuotojai_sqlalchemy.db')
Session = sessionmaker(bind=engine)
session = Session()

while True:
    pasirinkimas = int(input("Pasirinkite ką norite daryti: \n1 - Atvaizduoti visus darbuotojus \n2 - Įvesti darbuotoją \n3 - Redaguoti darbuotoją \n4 - Ištrinkite darbuotoją \nPasirinkite: "))


    if pasirinkimas == 1:
        try:
            darbuotojai = session.query(Darbuotojas).all()
            if not darbuotojai:
                 raise Exception("Lentelė yra tuščia")
            print("----------------------")
            for darbuotojas in darbuotojai:
                print(darbuotojas)
            print("----------------------")
        except Exception as e:
                print(str(e))

    if pasirinkimas == 2:
        vardas = input("Įveskite darbuotojo vardą: ")
        pavarde = input ("Įveskite darbuotojo pavardę: ")
        atlyginimas = float(input("Įveskite darbuotojo atlyginimą: "))
        dirba_str = input("Įveskite nuo kada darbuotojas dirba (formatas YYYY-MM-DD): ")
        dirba_nuo = datetime.strptime(dirba_str, '%Y-%m-%d').date()
        darbuotojas = Darbuotojas(vardas, pavarde, atlyginimas, dirba_nuo)
        session.add(darbuotojas)
        session.commit()


    if pasirinkimas == 3:
        darbuotojai = session.query(Darbuotojas).all()
        print("--------------------------")
        for darbuotojas in darbuotojai:
             print(darbuotojas)
        print("--------------------------")
        keiciamas_id = int(input("Pasirinkite norimo redaguoti darbuotojo ID: "))
        keiciamas_darbuotojas = session.query(Darbuotojas).get(keiciamas_id)
        pakeitimas = int(input("Ką norite pakeisti: 1 - Vardą,   2 - Pavardę,  3 - Atlyginimą,  4 - Nuo kada dirba  \n Pasirinkite: "))
        if pakeitimas == 1:
            keiciamas_darbuotojas.vardas = input("Įveskite naują vardą: ")
        if pakeitimas == 2:
            keiciamas_darbuotojas.pavarde = input("Įveskite naują pavardę: ")
        if pakeitimas == 3:
            keiciamas_darbuotojas.atlyginimas = float(input("Įveskitę naują atlyginimą: "))
        if pakeitimas == 4:
            dirba_str = input("Įveskite naują datą, nuo kada darbuotojas dirba (formatas YYYY-MM-DD): ")
            keiciamas_darbuotojas.dirba_str = dirba_str
            keiciamas_darbuotojas.dirba_nuo = date.fromisoformat(dirba_str)

        session.commit()

    
    if pasirinkimas == 4:
        darbuotojai = session.query(Darbuotojas).all()
        print("-------------------------------------")
        for darbuotojas in darbuotojai:
            print(darbuotojas)
        print("-------------------------------------")
        keiciamas_id = int(input("Pasirinkite norimo ištrinti darbuotojo ID: "))
        trinamas_darbuotojas = session.query(Darbuotojas).get(keiciamas_id)
        session.delete(trinamas_darbuotojas)
        session.commit()
