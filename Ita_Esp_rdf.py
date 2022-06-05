from rdflib import Graph, Literal, Namespace, URIRef, BNode
from rdflib.namespace import RDF, RDFS, NamespaceManager
import rdfpandas
import pandas as pd
import numpy as np
from rdflib.term import Identifier
import re

df = pd.read_csv("Ita_Esp_end.csv")

g = Graph()

dbo = Namespace("http://www.dbpedia.org/ontology/")
g.bind("dbo", dbo)
dbr = Namespace("http://www.dbpedia.org/resource/")
g.bind("dbr", dbr)

dbp = Namespace("http://www.dbpedia.org/page/")
#g.bind("dbp", dbp)

uriIsced = Namespace("http://www.example.org/isced/")
g.bind("uriIsced", uriIsced)

poi = g.resource(dbr.University)

iscritti = {}
laureati = {}
anni = {}
anniL = {}

#numero di iscritti per anno
for (x,y) in zip(df["year"], df["enrolled"]):
    if x in anni:
        anni[x] += y
    else:
        anni[x] = y

for x,y in anni.items():
    g.add([URIRef(dbp[str(x)]), URIRef(dbo.enrolled), Literal(str(y))])
    
for (x,y) in zip(df["year"], df["graduated"]):
    if x in anniL:
        anniL[x] += y
    else:
        anniL[x] = y

#numero di laureati per anno
for x,y in anniL.items():
    g.add([URIRef(dbp[str(x)]), URIRef(dbo.graduated), Literal(str(y))])

#numero di iscritti per codice ISCED
for ((x,y),z) in zip(zip(df["ISCED_F_2"], df["place"]), df["enrolled"]):
    if x in iscritti:
        iscritti[x] += z
    else:
        iscritti[x] = z
    g.add([URIRef(uriIsced[str(x)]), URIRef(dbo.place), Literal(str(y))])
    #definisce il tipo per il nostro soggetto
    g.add([URIRef(uriIsced[str(x)]), RDF.type, dbr.International_Standard_Classification_of_Education])
    
for x,y in iscritti.items():
    g.add([URIRef(uriIsced[str(x)]), RDF.type, dbr.International_Standard_Classification_of_Education])
    g.add([URIRef(uriIsced[str(x)]), URIRef(dbo.enrolled), Literal(str(y))])

#numero di laureati per codice ISCED
for ((x,y),z) in zip(zip(df["ISCED_F_2"], df["place"]), df["graduated"]):
    if x in laureati:
        laureati[x] += z
    else:
        laureati[x] = z
        
for x,y in laureati.items():
    g.add([URIRef(uriIsced[str(x)]), RDF.type, dbr.International_Standard_Classification_of_Education])
    g.add([URIRef(uriIsced[str(x)]), URIRef(dbo.graduated), Literal(str(y))])
    
    
#print(g.serialize(format='turtle'))
file = open("Ita_Esp_RDF.txt", "w")
file.write(g.serialize(format='turtle'))
file.close()