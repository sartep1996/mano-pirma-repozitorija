from darbuotojas_sqlachemy_backend import Darbuotojas
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import PySimpleGUI as sg
from datetime import datetime, date


engine = create_engine('sqlite:///darbuotojas_sql_alchemy_db/darbuotojai_sqlalchemy.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


class DarbuotojasGUI():

    def gauti_duomenis(self):
        self.darbuotojas_sarasas = session.query(Darbuotojas).all()
        duomenys = [[item.id, item.vardas, item.pavarde, item.atlyginimas, item.dirba_nuo]
            for item in self.darbuotojas_sarasas ]
        return duomenys
        
        
    
    def __init__(self):
        duomenys = self.gauti_duomenis()
        headers = ['ID', 'Vardas', "Pavardė", 'Atlyginimas', "Dirba nuo"]
        self.table = sg.Table(values=duomenys, headings=headers, auto_size_columns=True, key="-TABLE-")
        self.layout = [
            [self.table],
             [sg.Button ("Pridėti Darbuotoją",), sg.Button("Redaguoti Darbuotoją"), sg.Button("Ištrinti Darbuotoją"), sg.Button("Uždaryti")]]
        self.window = sg.Window("Darbuotojas", layout=self.layout)
        
    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED or event == 'Uždaryti':
                break
            elif event == 'Pridėti Darbuotoją':
                darbuotojas = self.prideti_darbuotoja()
                if isinstance (darbuotojas, Darbuotojas):
                    self.table.update(values=self.gauti_duomenis())
            elif event == 'Redaguoti Darbuotoją':
                selected_rows = values["-TABLE-"]
                if selected_rows:
                    selected_row = selected_rows[0]
                    selected_darbuotojas = self.darbuotojas_sarasas[selected_row]
                    self.redaguoti_darbuotoja(selected_darbuotojas)
                    if isinstance (selected_darbuotojas, Darbuotojas):
                        self.table.update(values=self.gauti_duomenis())
            elif event == 'Ištrinti Darbuotoją':
                selected_rows = values["-TABLE-"]
                if selected_rows:
                    selected_row = selected_rows[0]
                    selected_darbuotojas = self.darbuotojas_sarasas[selected_row]
                    self.istrinti_darbuotoja(selected_darbuotojas)
                    if isinstance (selected_darbuotojas, Darbuotojas):
                        self.table.update(values=self.gauti_duomenis())

           
        self.window.close()

    def istrinti_darbuotoja(self, darbuotojas):

        layout = [
            [sg.Text("Ar tikrai norite ištrinti darboutoją?")],
            [sg.Button("Taip", key="Taip"), sg.Button("Ne", key="Ne")]
        ]
        window_istrinti = sg.Window("Ištrinti Darbuotoją", layout=layout)

        while True:
            event, values = window_istrinti.read()
            if event in (None, "Ne"):
                window_istrinti.close()
                return event == "Ne"
            elif event == "Taip":
                try:
                    session.delete(darbuotojas)
                    session.commit()
                except:
                    sg.popup_error("Klaida bandant ištrinti darbuotoją")
                else:
                    sg.popup("Darbuotojas Ištrintas")
                    window_istrinti.close()


    def prideti_darbuotoja(self):

        layout = [
            [sg.Text("Įveskite darbuotojo vardą: "), sg.Input("", key = "vardas")],
            [sg.Text("Įveskite darbuotojo pavardę: "), sg.Input("", key = "pavardė")],
            [sg.Text("Įveskite darbuotojo atlyginimą: "), sg.Input("", key = "atlyginimas")],
            [sg.Text("Iveskite nuo kada dirba darbuotojas(formatas YYYY-MM-DD) : "), sg.Input("", key= "dirba_nuo")],
            [sg.Button("Patvirtinti", key="Patvirtinti"), sg.Button("Uždaryti", key="Uždaryti")]
        ]
        window_prideti = sg.Window("Pridėti Darbuotoją", layout=layout)

        while True:
            event, values = window_prideti.read()
            if event in (None, "Uždaryti"):
                window_prideti.close()
                return event == "Uždaryti" 
            elif event == "Patvirtinti":
                try:
                    darbuotojas = Darbuotojas(values["vardas"], 
                                              values["pavardė"], 
                                              values["atlyginimas"], 
                                              date.fromisoformat(values["dirba_nuo"]))
                    session.add(darbuotojas)
                    session.commit()
                except Exception as e:
                    print(f"An error occurred: {e}")
                else:
                    window_prideti.close()
                    return darbuotojas
    

    def redaguoti_darbuotoja(self, darbuotojas):
        layout = [
            [sg.Text("Vardas:"), sg.Input(darbuotojas.vardas, key="vardas")],
            [sg.Text("Pavarde:"), sg.Input(darbuotojas.pavarde, key="pavardė")],
            [sg.Text("Alga:"), sg.Input(str(darbuotojas.atlyginimas), key="atlyginimas")],
            [sg.Text("Dirba_nuo:"), sg.Input(darbuotojas.dirba_nuo, key="dirba_nuo")],
            [sg.Button("Atnaujinti", key="Atnaujinti"), sg.Button("Uždaryti", key="Uždaryti")]
        ]
        window_redaguoti = sg.Window("Redaguoti Darbuotoją", layout=layout)
       
        while True:
            event, values = window_redaguoti.read()
            if event in (None, "Uždaryti"):
                window_redaguoti.close()
                return None
                # return event == "Uždaryti" 
            elif event == "Atnaujinti":
                try:
                    darbuotojas.vardas = values["vardas"]
                    darbuotojas.pavarde = values["pavardė"]
                    darbuotojas.atlyginimas = values["atlyginimas"]
                    darbuotojas.dirba_nuo = datetime.strptime(values["dirba_nuo"], '%Y-%m-%d')
                    session.add(darbuotojas)
                    session.commit()
                except Exception as e:
                    print(f"An error occurred: {e}")
                else:
                    window_redaguoti.close()
                    return darbuotojas

darbuotojai = DarbuotojasGUI()
darbuotojai.run()
        