import pandas as pd
from src.constants.path import LAB_1_ROOT

def get_database(): 
    return pd.read_csv(f"{LAB_1_ROOT}/src/data/drinking_water_potability-1100.csv")