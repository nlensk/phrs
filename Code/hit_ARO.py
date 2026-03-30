# make a dictionary where the key is the alignment slengths and the values are how often they occur.

f = open("NC_042128.1_300hits.txt", "r")
d = {}


for lines in f:
        ARO = lines.split("\t")[1]
        three = ARO.split("|")[5]
        three = three.split("-")[0]
        ARO = ARO.split("|")[4]
        
        if three not in d:
            d[three] = []
        d[three].append(ARO)
        
        
for element in d:
    print(element, len(d[element]))
    

f.close()

