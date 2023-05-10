import sqlite3

conn = sqlite3.connect('automobiliai.db')
c = conn.cursor()

query = """
CREATE TABLE IF NOT EXISTS masina(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    marke VARCHAR(50),
    modelis VARCHAR(50),
    spalva VARCHAR (50),
    pagaminimo_metai VARCHAR (50),
    kaina INTEGER
);
"""
with conn:
    c.execute(query)
    conn.commit()


insert_masina_query = ''' INSERT INTO masina
(marke, modelis, spalva, pagaminimo_metai, kaina)
VALUES ('Ford', 'Model T', 'juoda', 1910, 25000)
'''
with conn:
    c.execute(insert_masina_query)
    conn.commit()

insert_masina_query = ''' INSERT INTO masina
(marke, modelis, spalva, pagaminimo_metai, kaina)
VALUES ('Studbaker', 'Dictator', 'zalia', 1927, 40000)
'''
with conn:
    c.execute(insert_masina_query)
    conn.commit()

insert_masina_query = ''' INSERT INTO masina
(marke, modelis, spalva, pagaminimo_metai, kaina)
VALUES ('Chevrolet', 'Series CA', 'melyna', 1933, 50000)
'''

with conn:
    c.execute(insert_masina_query)
    conn.commit()
