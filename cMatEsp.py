import matplotlib.pyplot as plt
import numpy as np
import pandas 

mat = pandas.read_csv("mat.csv")

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
mat.to_csv("Mat_end.csv")
mat = pandas.read_csv("Mat_end.csv")
#print(mat)

#utilizziamo dei dizionari per pulire il dataset (alcune stringhe presentano caratteri "strani" a causa della codifica diversa dall'uft-8)
uncorrected =np.sort(np.unique(mat["region (public/private)"]))

corrected = ['Andalucía (Pública) ', 'Andalucía (Privada) ', 'Aragón (Pública) ',
 'Aragón (Privada) ', 'Asturias(Principadode) (Pública) ',
 'Asturias(Principadode) (Privada) ', 'Balears(Illes) (Pública) ', 
 'Balears(Illes) (Privada) ', 'Canarias (Pública) ',  'Canarias (Privada) ', 
 'Cantabria (Pública) ', 'Cantabria (Privada) ', 
 'Castilla-LaMancha (Pública) ', 'Castilla-LaMancha (Privada) ', 
 'CastillayLeón (Pública) ', 'CastillayLeón (Privada) ', 
 'Cataluna (Pública) ', 'Cataluna (Privada) ', 
 'ComunitatValenciana (Pública) ', 'ComunitatValenciana (Privada) ', 
 'Estado (Pública) ', 'Estado (Privada) ',  'Extremadura (Pública) ', 
'Extremadura (Privada) ', 'Galicia (Pública) ', 'Galicia (Privada) ', 
 'Madrid(Comunidadde) (Pública) ','Madrid(Comunidadde) (Privada) ', 
'Murcia(Regiónde) (Pública) ',  'Murcia(Regiónde) (Privada) ', 
 'Navarra(ComunidadForalde) (Pública) ', 
 'Navarra(ComunidadForalde) (Privada) ', 'PaísVasco (Pública) ',
'PaísVasco (Privada) ', 'Rioja(La) (Pública) ', 'Rioja(La) (Privada) ']
correct = dict(zip(uncorrected,corrected))
corrected = [correct.get(x) for x in mat["region (public/private)"]]
mat["region (public/private)"] = corrected

mat.rename(columns = {"values" : "matr"}, inplace = True)

mat.to_csv("Mat_end.csv",  index = True)