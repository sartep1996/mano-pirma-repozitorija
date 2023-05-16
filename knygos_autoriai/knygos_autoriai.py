import os
from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine, Table, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///knygos_autoriai/authors2books_test.db')
Base = declarative_base()

sasaju_lentele = Table('sasajos', Base.metadata,
    Column('autorius_id', Integer, ForeignKey('autorius.id')),
    Column('knyga_id', Integer, ForeignKey ('knyga.id'))
)

class Autorius(Base):
    __tablename__ = 'autorius'
    id = Column(Integer, primary_key=True)
    vardas = Column("Vardas", String)
    pavarde = Column("Pavarde", String)
    knygos = relationship("Knyga", secondary=sasaju_lentele, back_populates="autoriai")

    def __str__(self):
        return f"Autorius {self.id}: {self.vardas} {self.pavarde}"

class Knyga(Base):
    __tablename__ = 'knyga'
    id = Column(Integer, primary_key=True)
    pavadinimas = Column("Pavadinimas", String)
    isleidimo_metai = Column("Isleidimo Metai", Integer)
    autoriai = relationship("Autorius",secondary=sasaju_lentele, back_populates="knygos")

    def __str__(self):
        return f"Knyga {self.id}: {self.pavadinimas} ({self.isleidimo_metai})"


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()




def prideti_autoriu(vardas, pavarde):
    autorius = Autorius(vardas=vardas, pavarde=pavarde)
    session.add(autorius)
    session.commit()

def prideti_knyga(pavadinimas, isleidimo_metai, autoriai):
    knyga = Knyga(pavadinimas=pavadinimas, isleidimo_metai=isleidimo_metai, autoriai=autoriai)
    session.add(knyga)
    session.commit()

def print_sasaju_lentele():
   result = session.execute(sasaju_lentele.select())
   for eile in result.fetchall():
       print(eile)

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
   
   
    # with engine.connect() as conn:
    #     stmt = select([sasaju_lentele])
    #     result = conn.execute(stmt)

    #     print("Autorius_ID/Knygos_ID")
    #     for row in result:
    #         print(f"{row[0]}\t\t{row[1]}")

while True:
    print("Pasirinkite: \n 1 - Peržiūrėti visas knygas \n 2 - Peržiūrėti visus autorius \n 3 - Peržiūrėti autorius ir knygas \n 4 - Pridėti autorių \n 5 - Pridėti knygą \n 6 - Išeiti ")

    choice = int(input("Įveskite savo pasirinkimą: "))

    if choice == 1:
        lentele = session.query(Knyga).all()
        for autorius in lentele:
            print(autorius)


    if choice == 2:
        clear()
        lentele = session.query(Autorius).all()
        for knyga in lentele:
            print(knyga)

    if choice == 3:
        clear()
        print_sasaju_lentele()

    if choice == 4:
        clear()
        vardas = input("Įveskite autoriaus vardą: ")
        pavarde = input("Įveskite autoriaus pavardę: ")
        prideti_autoriu(vardas, pavarde)

    if choice == 5:
        clear()
        pavadinimas = input("Įveskite knygos pavadinimą: ")
        isleidimo_metai = int(input("Įveskite išleidimo metus: "))
        autoriai = int(input("Įveskite autoriaus ID"))
        prideti_knyga(pavadinimas, isleidimo_metai, autoriai)

    if choice == 6:
        clear()
        break


 








# autorius1 = Autorius(vardas= "Alexandre", pavarde = "Dumas")
# autorius2 = Autorius(vardas= "Jules", pavarde = "Verne")
# autorius3 = Autorius(vardas= "Victor", pavarde = "Hugo" )
# knyga1 = Knyga(pavadinimas = "Trois Mousequetaires", isleidimo_metai = 1844)
# knyga2 = Knyga(pavadinimas = "Le Tour du monde en quatre-vingts jours", isleidimo_metai = 1872)
# knyga3 = Knyga(pavadinimas = "Notre Dame de Paris", isleidimo_metai = 1831)
# knyga4 = Knyga(pavadinimas = "Les Miserables", isleidimo_metai = 1862)

# autorius1.knygos.append(knyga1)
# autorius2.knygos.append(knyga2)
# autorius3.knygos.append(knyga3)
# autorius3.knygos.append(knyga4)

# session.add(autorius1)
# session.add(autorius2)
# session.add(autorius3)
# session.commit()