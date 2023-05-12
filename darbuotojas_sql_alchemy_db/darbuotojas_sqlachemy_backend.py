from sqlalchemy import Column, Integer, String, Float, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base



engine = create_engine('sqlite:///darbuotojas_sql_alchemy_db/darbuotojai_sqlalchemy.db')
Base = declarative_base()

class Darbuotojas(Base):
    __tablename__= 'Darbuotojas'
    id = Column(Integer, primary_key=True)
    vardas = Column("Vardas", String)
    pavarde = Column("Pavarde", String)
    atlyginimas = Column("Atlyginimas", Float)
    dirba_nuo = Column(Date, name= 'Dirba_nuo')


    def __init__(self, vardas, pavarde, atlyginimas, dirba_nuo):
        self.vardas = vardas
        self.pavarde = pavarde
        self.atlyginimas = atlyginimas
        self.dirba_nuo = dirba_nuo

    def __repr__(self):
        return f'{self.id, self.vardas, self.pavarde, self.atlyginimas, self.dirba_nuo}'
    

Base.metadata.create_all(engine)
