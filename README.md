### Progetto Open Data

Per ottenere i singoli dataset ripuliti(Egr_end.csv, Mat_end.csv, Mat_ita_end.csv, Lau_end.csv):
```
python cEgrEsp.py 
python cMatEsp.py 
python cMat.py 
python cLaur.py 
```

per ottenere i dataset contenenti i dati complessivi dei due paesi (Spagnoli.csv, Italiani.csv)
```
python Esp_end.py 
python Ita_end.py
```

Infine eseguire per ottenere il dataset finale (Ita_Esp_end.csv)
```
python ita_esp.py 
```

Una volta ottenuto il dataset finale, eseguire per generare il file Ita_Esp_RDF.ttl
```
python Ita_Esp_rdf.py 
```
