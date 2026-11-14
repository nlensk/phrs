"""
@author: Nadia Lenskaia 2025
All rights reserved.
"""
# This code takes a BLAST file and creates a dictionary where the keys are the positions (formatted as start:end) and the values are how often they occur

f = open("BLAST.txt", "r")
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
