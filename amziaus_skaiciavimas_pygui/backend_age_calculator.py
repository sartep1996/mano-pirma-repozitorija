import PySimpleGUI as sg
import datetime


def calculate_current_year():
    current_year = datetime.datetime.now().year
    years_to_hundred = current_year + (100 - int(current_year))


