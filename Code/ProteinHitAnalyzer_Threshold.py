"""
@author: Nadia Lenskaia 2025
All rights reserved.
"""

#This code compares the length of the hit to the length of its resitome
fname = "card_proteins.fasta"
f = open(fname, "r")
lines = f.readlines()
f.close()

#This function creates a dictionary where the AROs are the keys and their resistome sequences are the values
def aroDict(t, daro):
    aro = t[0].split("|")[2].split(":")[1]
    seq = ""
    x = t[1:]
    for item in x:
        seq += item
    daro[aro] = seq
    return daro    


daro = {}
t = []
for line in lines:
    if line[0] == ">":
        if t != []:
            daro = aroDict(t, daro)
            t = []
    line = line.strip()
    t.append(line)
    
daro = aroDict(t, daro)
     
'''    
for z in daro:
    print(z, daro[z])
'''







#This code creates a dictionary from a list of hits in the input file where the genome ids are the keys and the hit information is the values
path = "C:\\Users\\nalen\\OneDrive\\Desktop\\ayy phage research and stuff woohoo\\bioinfo\\Phage_ Card\\CARD_Resistomes_ONLY_duplicates\\results\\"
fname = "6_results_proteins.out"
f = open(path + fname, "r")
lines = f.readlines()
f.close()

#lines = lines[1:]
d = {}

for line in lines:
    line = line.strip()
    line = line.split("\t")
    line[1]  = line[1].split("|")[2]
    gid = line[0]
    if gid not in d:
        d[gid] =  []
    d[gid].append(line)   
    #break
    
#print(d)
counter = 0
thresh = 70
#-------------------------------------------------------  
#fout = open("lengthProteinHitsResults_test1.txt", "w")
sp="\t"
fout = open("log2.0_70.txt", "w")
print("gid", "# of hits", "threshold", "hits above threshold", file=fout, sep=sp)
for gid in d:
    t_hits = d[gid]
    for hit in t_hits:
        aro = hit[1].split(":")[1]
        hitLength = int(hit[3])
        bitScore = hit[-1]
        perItent = hit[2]
        aroLength = 0
        if aro in daro:
            aroLength = len(daro[aro])
        if aroLength > 0:
            percent = (hitLength / aroLength) * 100
            #print(gid, aro, hitLength, aroLength, perItent, bitScore, round(percent, 2), file = fout, sep = "\t")
            if (float(perItent) > thresh) and (percent > thresh):
                counter += 1
    print(gid, len(t_hits), thresh, counter, file=fout, sep=sp)
    counter = 0        
    #break
fout.close()
