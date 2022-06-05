import matplotlib.pyplot as plt
import numpy as np
import pandas 
import re

lau = pandas.read_csv("Laureati.csv")

lau.drop(["IstatP"], axis = 1, inplace = True) #non ci interessa

#rinominiamo la colonna AnnoS, con Anno
lau.rename(columns = {"AnnoS" : "Anno"}, inplace = True)

#inserimento colonne genere e laureati
laureati = pandas.DataFrame()

for x in lau[:-2]:
    laureati[x] = [*lau[x], *lau[x]]

laureati["laureati"] = [*lau["Lau_M"], *lau["Lau_F"]]  
maschi = ["M"]*len(lau)
femmine = ["F"]*len(lau)
laureati["SESSO"] = [*maschi, *femmine]

laureati.drop(["Lau_M"], axis = 1, inplace = True)
laureati.drop(["Lau_F"], axis = 1, inplace = True)

#inserimento codice ISCED con l'ausilio di un dizionario
foet = pandas.read_csv("cod_foet2013.csv")
foetDictionary = [(x,y) for x,y in zip(foet["Classe"],foet["ISCED_F_2dgt"]) if x[0] == "L"]
foetDictionary = dict(foetDictionary)
laureati.drop(laureati[laureati.ClasseNUMERO.astype(str).str[0] != "L"].index, inplace=True)
laureati["ISCED_F_2dgt"] = [foetDictionary.get(x) for x in laureati["ClasseNUMERO"]]
laureati = laureati.drop(["_id","ClasseNUMERO","CorsoNOME"],axis=1)
laureati = laureati.groupby(['Anno', 'AteneoCOD', 'AteneoNOME', 'SedeC', 'ISCED_F_2dgt', 'SESSO']).sum()

laureati.to_csv("Lau_end.csv",  index = True)