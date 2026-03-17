"""
@author: Nadia Lenskaia 2025
All rights reserved.
"""
# This code creates a dictionary where the headers are the keys and the sequences are the values
# Only works for individual sequence fasta files

def genomestring(t):
    header = t[0]
    header = header.strip()
    header = header.split(" |")
    header = header[0]
    header = header[1:]

    t = t[1:]
    genome = ""
    
    for line in t:
        #ff.write(line)
        line = line.strip()
        genome += lin    
        
    return [header, genome]
    

fname = "example.fasta"
f = open(fname, "r")
t1 = f.readlines()
f.close()

res = genomestring(t1)
print(res[0], len(res[1]))
