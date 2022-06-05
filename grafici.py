import matplotlib.pyplot as plt
import numpy as np
import pandas 

dfI = pandas.read_csv("Italiani.csv")
dfS = pandas.read_csv("Spagnoli.csv")

dfI.drop(["Unnamed: 0"], axis = 1, inplace = True)
dfS.drop(["Unnamed: 0"], axis = 1, inplace = True)

print([x for x in dfI])
print([x for x in dfS])

dfI1 = dfI.groupby(["ISCED_F_2dgt", "SESSO", "Anno"]).sum() #italiani
dfS1 = dfS.groupby(["ISCED_f_2", "gender", "year"]).sum() #spagnoli

dfI1.to_csv("ItalianiGraph.csv")
dfS1.to_csv("SpagnoliGraph.csv")

dfI1 = pandas.read_csv("ItalianiGraph.csv")
dfS1 = pandas.read_csv("SpagnoliGraph.csv")

# 61 informatica
# 22 filosofia
# 71 ingegneria meccanica 

isced = ["61", "22", "71"]
gender = ["M", "F"]

dfS1["gender"] = ["M" if x == "Hombres" else "F" for x in dfS1["gender"]]

iscrI = []
lauI = []
iscrS = []
lauS = []

for i in range(3):
    for j in range(2):
        lauI.append([(x,z) for x,y,s,z in zip(dfI1["laureati"], dfI1["ISCED_F_2dgt"], dfI1["SESSO"], dfI1["Anno"]) if str(int(y)) == isced[i] and s == gender[j]])
        lauS.append([(x,z) for x,y,s,z in zip(dfS1["egr"], dfS1["ISCED_f_2"], dfS1["gender"], dfS1["year"]) if str(int(y)) == isced[i] and s == gender[j]])
        iscrI.append([(x,z) for x,y,s,z in zip(dfI1["Imm"], dfI1["ISCED_F_2dgt"], dfI1["SESSO"], dfI1["Anno"]) if str(int(y)) == isced[i] and s == gender[j]])
        iscrS.append([(x,z) for x,y,s,z in zip(dfS1["matr"], dfS1["ISCED_f_2"], dfS1["gender"], dfS1["year"]) if str(int(y)) == isced[i] and s == gender[j]])

anni = []
graphs = [lauI, lauS, iscrI, iscrS]
colors = ["blue", "cornflowerblue", "red", "salmon"]
labels = ["italiani", "italiane", "spagnoli", "spagnole"]
titles = ["laureati", "iscritti"]
iscedName = ["Information and Communication Technologies (ICTs)", "Humanities" , "Engineering, manufacturing and construction"]

for i in range(3):
    for k in range(4):
        for j in range(2):
            anni = [x[1] for x in graphs[k][i*2+j]]
            dati = [x[0] for x in graphs[k][i*2+j]]
            plt.plot(anni, dati, color = colors[(k%2)*2 + j], label = labels[(k%2)*2 + j])
        if (k+1)%2 == 0:
            plt.title(titles[k//2] + " " + iscedName[i])
            plt.savefig(titles[k//2] + iscedName[i] + ".png")
            plt.show()
        
    
# subjects = np.unique([s for s in dfI["ISCED_F_2dgt"]])

# for sub in subjects:
#     print(sub)
#     matBySub = dfI.drop(dfI[dfI.ClasseNOME != sub].index)
#     M = matBySub.drop(matBySub[matBySub.SESSO != "M"].index)
#     F = matBySub.drop(matBySub[matBySub.SESSO != "F"].index)
#     M = M["Imm"]
#     F = F["Imm"]
#     years = [i for i in range(2015,2021)]
#     plt.plot(years, F,color = "purple",label="female")
#     plt.plot(years, M,color = "crimson",label="male")
#     plt.show()