import matplotlib.pyplot as plt
import numpy as np
import pandas 
import re

#join tra i datasets spagnoli

egrEsp = pandas.read_csv("Egr_end.csv") #laureati
matEsp = pandas.read_csv("Mat_end.csv") #immatricolati

#creiamo un unico dataset per i dati italiani
esp = pandas.merge(matEsp, egrEsp, how='inner', on = ["ISCED_f_2", "gender", "year", "region (public/private)"])

esp.drop(["Unnamed: 0_x"], axis = 1, inplace = True)
esp.drop(["Unnamed: 0_y"], axis = 1, inplace = True)

esp.to_csv("Spagnoli.csv",  index = True)