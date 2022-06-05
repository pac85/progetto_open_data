import matplotlib.pyplot as plt
import numpy as np
import pandas 

ita = pandas.read_csv("Italiani.csv")
esp = pandas.read_csv("Spagnoli.csv")

ita.drop(["Unnamed: 0"], axis = 1, inplace = True)
esp.drop(["Unnamed: 0"], axis = 1, inplace = True)
ita.drop(["AteneoCOD"], axis = 1, inplace = True)
ita.drop(["SedeC"], axis = 1, inplace = True)

ita.rename(columns = {"ISCED_F_2dgt" : "ISCED_F_2","Anno" : "year", "SESSO" : "gender", "Imm" : "enrolled", "laureati" : "graduated", "AteneoNOME" : "place"}, inplace = True)
esp.rename(columns = {"ISCED_f_2" : "ISCED_F_2","matr" : "enrolled", "egr" : "graduated", "region (public/private)" : "place"}, inplace = True)

result = pandas.concat([ita, esp]) #creiamo un dataset complessivo 

#convertiamo i valori di queste colonne in interi (prima erano double)
result["ISCED_F_2"] = result["ISCED_F_2"].apply(lambda a: int(a))
result["graduated"] = result["graduated"].apply(lambda a: int(a))
result["enrolled"] = result["enrolled"].apply(lambda a: int(a))

result.to_csv("Ita_Esp_end.csv", index = True)