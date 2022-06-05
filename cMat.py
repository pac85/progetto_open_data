import matplotlib.pyplot as plt
import numpy as np
import pandas 
import re

immatricolati = pandas.read_csv("Immatricolati.csv")

#rinominiamo la colonna AnnoA, con Anno
immatricolati.rename(columns = {"AnnoA" : "Anno"}, inplace = True)

#uniformità con gli altri dataset
immatricolati["Anno"] = immatricolati["Anno"].apply(lambda a: a.split("/")[0]) 

#inserimento codice ISCED con l'ausilio di un dizionario
foet = pandas.read_csv("cod_foet2013.csv")
foetDictionary = [(x,y) for x,y in zip(foet["Classe"],foet["ISCED_F_2dgt"]) if x[0] == "L"]
foetDictionary = dict(foetDictionary)
immatricolati.drop(immatricolati[immatricolati.ClasseNUMERO.astype(str).str[0] != "L"].index, inplace=True)
immatricolati["ISCED_F_2dgt"] = [foetDictionary.get(x) for x in immatricolati["ClasseNUMERO"]]
immatricolati = immatricolati.drop(["_id","ClasseNUMERO","ClasseNOME"],axis=1)
immatricolati = immatricolati.groupby(['Anno', 'ISCED_F_2dgt', 'SESSO']).sum()


immatricolati.to_csv("Mat_ita_end.csv",  index = True)