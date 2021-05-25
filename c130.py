import csv

import pandas as pd


df = pd.read_csv("total_stars.csv")

print(df.shape)

del df["Unnamed: 0"]

del df["Unnamed: 6"]

del df["Star_name.1"]

del df["Distance.1"]

del df["Mass.1"]

del df["Luminosity"]

del df["Radius.1"]

df.to_csv('final_data.csv')
