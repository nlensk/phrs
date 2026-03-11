"""
@author: Nadia Lenskaia 2025
All rights reserved.
"""

# This script outputs sequence lengths in a file

file = open("sequence_file.fasta", "r")
lines = file.readlines()
file.close()
fOut = open("output_sequence_file.txt", "w")

counter = 0
d = {}

for line in lines:
    if ">" in line:
        line = line.split(">")[1]
        line = line.split(" ")[0]
        if line not in d:
            d[line] = ""
            

for line in lines:
    if ">" in line:
        dline = line
        line = line.split(">")[1]
        line = line.split(" ")[0]
        if line in d:
            pos = lines.index(dline)
            seq = lines[pos + 1]
            while ">" not in seq:
                d[line] += seq
                seqpos = lines.index(seq)
                seq = lines[seqpos + 1]
            # The line below can be uncommented to check if there are sequences above a certain length. Defult = 20000 characters    
            #if len(d[line]) > 20000:
            print(line, len(d[line]), file=fOut, sep="\t")
            
         
fOut.close()
                
    
#print(d)
#print(len(d))
