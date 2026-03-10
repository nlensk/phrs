"""
@author: Nadia Lenskaia 2025
All rights reserved.
"""

# This code checks if the ids in a pair of nucleotide and protein files overlap

fname = "ALLLLL_nucleotides.out"
f = open(fname, "r")
ids = []
t_ids = []

for line in f:
    if "NC_" in line:
        ids.append(line)
    
for line in ids:
    line = line.split("|")[0]
    line = line.split("\\")[0]
    t_ids.append(line[0:11])

#print(t_ids)
#print(t_ids)


f.close()

fname = "ALLLLL_protein.out"
f = open(fname, "r")
pids = []
t_pids = []

for line in f:
    if "NC_" in line:
        pids.append(line)
    
for line in pids:
    line = line.split("|")[0]
    line = line.split("\\")[0]
    t_pids.append(line[0:11])
    #print(t_pids)
    #input()

f.close()


t_ids = [1, 1, 5]
t_pids = [1, 1, 1, 1, 5, 5, 3]

for element in t_ids:
    if element not in t_pids:
        print(element + "NOT INM PIDS")
    

print(len(t_ids), len(t_pids))