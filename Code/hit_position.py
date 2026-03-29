"""
@author: Nadia Lenskaia 2025
All rights reserved.
"""
# This code analyzes the location of blast hits in a text file.
# One can use this code to check the location of hits.

f = open("hit_example.txt", "r")
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

