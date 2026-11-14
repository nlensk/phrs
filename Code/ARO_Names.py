# This code creates a dictionary where the keys are the ARO names (e.g. SHV, TEM) and the values are the AROS associated with them

f = open("hits.txt", "r")
d = {}


for lines in f:
        ARO = lines.split("\t")[1]
        name = ARO.split("|")[5]
        name = name.split("-")[0]
        ARO = ARO.split("|")[4]
        
        if name not in d:
            d[name] = []
        d[name].append(ARO)
        
        
for element in d:
    print(element, len(d[element]))
    

f.close()
