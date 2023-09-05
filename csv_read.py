print('start met csv uitlees applicatie')

import pandas # andermans code (ook wel Library - Dependency - Packages)

df = pandas.read_csv('pokemon.csv')
print(df["Name"]) # print de namen van de pokemons

for r,rij in df.iterrows():
    print(rij["Name"])
    print("De naam van de pokemon is " + rij["Name"])
    