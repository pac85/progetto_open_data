import matplotlib.pyplot as plt
import numpy as np
import pandas 
import re

mat = pandas.read_csv("egr.csv")

mat["year"] = mat["year"].apply(lambda a: a.split("-")[0]) #uniformità con gli altri dataset

mat.drop(mat[mat.region == "Total"].index, inplace=True)     #eliminare i totali per regione
mat.drop(mat[mat["type(public, private)"] == "Total"].index, inplace=True) #considerare la distinzione tra pubblica e privata
mat.drop(mat[mat.precence != "Total"].index, inplace=True)   #eliminare la distinzione presenza e non presenza
mat.drop(mat[mat.location != "Total"].index, inplace=True)   #per maschi e femmine considerare il totale, senza distinzioni
mat.drop(mat[mat.gender == "Ambossexos"].index, inplace=True) #considerare la distinzione maschi e femmine, rimuovendo i totali
mat.drop(mat[mat.subject == "Total"].index, inplace=True)    #eliminare i totali per corso
mat.drop(["precence"], axis = 1, inplace = True)
mat.drop(["location"], axis = 1, inplace = True)

#considerare la differenza tra pubblica e privata, la coppia (pubblica/privata, regione) diventa un solo attributo
mat["region (public/private)"] = [x + " (" + y + ") " for x,y in zip(mat["region"], mat["type(public, private)"])]  
mat.drop(["region"], axis = 1, inplace = True)
mat.drop(["type(public, private)"], axis = 1, inplace = True)

#inserimento colonna con codice ISCED
mat["ISCED_f_2"] = [x.split(" ")[0][:3] for x in mat["subject"]]
temp = []
for x in mat["ISCED_f_2"]:
    temp.append(len(x) == 2)
mat.drop(mat[temp].index, inplace=True)

#somma i valori in "values" secondo le condizioni nel groupby
mat = mat.groupby(["ISCED_f_2", "gender", "year", "region (public/private)"]).sum()
mat.to_csv("Egr_end.csv")
mat = pandas.read_csv("Egr_end.csv")

mat.rename(columns = {"values" : "egr"}, inplace = True)

mat.to_csv("Egr_end.csv", index = True)