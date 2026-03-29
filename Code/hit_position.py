# make a dictionary where the key is the alignment slengths and the values are how often they occur.

f = open("NC_042128.1_300hits.txt", "r")
d = {}


for lines in f:
        qstart = lines.split("\t")[6]
        qend = lines.split("\t")[7]
        pos = qstart + ":"  + qend
        
        if pos not in d:
            d[pos] = 1
        else:
            d[pos] += 1
    

for position in d:
    print(position, d[position])    
            
    













f.close()

