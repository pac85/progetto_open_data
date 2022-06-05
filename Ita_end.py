import matplotlib.pyplot as plt
import numpy as np
import pandas 
import re

#join tra i datasets italiani

lauIta = pandas.read_csv("Lau_end.csv") #laureati
matIta = pandas.read_csv("Mat_ita_end.csv") #immatricolati

#creiamo un unico dataset per i dati italiani
ita = pandas.merge(matIta, lauIta, how='inner', on = ["ISCED_F_2dgt", "SESSO", "Anno"])

ita.to_csv("Italiani.csv",  index = True)