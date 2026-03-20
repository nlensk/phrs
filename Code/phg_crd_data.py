"""
@author: Nadia Lenskaia 2025
All rights reserved.
"""
# This code creates a dictionary where the headers are the keys and the sequences are the values

''''''
t_seq = []
''''''

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


"""

for line in f:
    if ">" in line[0]:
        if t_seq != []:
            res = genomestring(t_seq)
            seq_id = res[0]
            seq = res[1]
            n_seq = len(seq)
            print(seq_id, n_seq)
            t_seq = []
    t_seq.append(line)

res = genomestring(t_seq)
seq_id = res[0]
seq = res[1]
n_seq = len(seq)
print(seq_id, n_seq)

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
