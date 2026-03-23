# This code allows you to extract fasta sequences for the purpose of further analysis


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


t_seq = []

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
