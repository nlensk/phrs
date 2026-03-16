"""
@author: Nadia Lenskaia 2025
All rights reserved.
"""

# splits header and genomes and can be used to find the length of sequences

path = "C:\\bioinfo\\Phage_ Card\\"
fname = "numbers.txt"
d = {}
f = open(path + fname, "r")

for line in f: 
    line = line.strip()
    t_line = line.split("\t")
    ##print(t_line)
    d[t_line[0]] = int(t_line[1])
    #print(d)
    #break
#print(d)

f.close()


#if "NC_001825.1" in d:
    #print(d["NC_001825.1"])
    
    
    
    
  
path = "C:\\bioinfo\\Phage_ Card\\"
fname = "sequences.fasta"
#fname = "test.fasta"
f = open(path + fname, "r")
t_seq = []




def genomestring(t):
    
    
    header = t[0]
    header = header.strip()
    header = header.split(" |")
    header = header[0]
    header = header[1:]
    
    #ff = open(path + "fna\\" + header + ".fasta", "w")
    #ff.write(t[0])
    
    #print(header)
    t = t[1:]
    genome = ""
    
    for line in t:
        #ff.write(line)
        line = line.strip()
        genome += line
        
    #print(genome)        
        
    
    #print(header, t)
    #ff.close()
    return [header, genome]
    

fname = "NC_048030.1.fasta"
f = open(path + "fna\\" + fname, "r")
t1 = f.readlines()
f.close()

res = genomestring(t1)
print(res[0], len(res[1]))


"""

for line in f:
    if ">" in line[0]:
        if t_seq != []:
            res = genomestring(t_seq)
            seq_id = res[0]
            seq = res[1]
            n_seq = len(seq)
            
            if seq_id in d:
                if d[seq_id] != n_seq:
                    print("ERRORORORORORO" + seq_id)
                    break
                #else:
                    #print("check yay" + seq_id)
            #print(t_seq)
            t_seq = []
    t_seq.append(line)

res = genomestring(t_seq)
seq_id = res[0]
seq = res[1]
n_seq = len(seq)

if seq_id in d:
    if d[seq_id] != n_seq:
        print("ERRORORORORORO" + seq_id) 
    else:
        print("check yay" + seq_id)

    
    #print(t_seq)
    #input()

f.close()


"""



'''
# outputs name and number of letters in a genome 

path = "C:\\bioinfo\\Phage_ Card\\"
fname = "sequences.tsv"
#fname = "test.fasta"
f = open(path + fname, "r")
lines = f.readlines()
f.close()

#print(len(lines))
lines = lines[1:]
#print(len(lines))
#print(lines[0])
fout = open(path + "numbers.txt", "w")


for line in lines:
    #print(line)
    t_line = line.split("\t")
    print(t_line[0], t_line[14])
    fout.write(t_line[0] + "\t" + t_line[14] + "\n")
    

fout.close()




# Outputs # of > in fasta file
path = "C:\\bioinfo\\Phage_ Card\\"
fname = "sequences.fasta"
#fname = "test.fasta"
f = open(path + fname, "r")
carrots = 0
print(carrots)

for line in f:
    #print(line[0])
    if ">" in line[0]:
        carrots += 1
        
print(carrots)

f.close()

print("YIPPEE")
'''
