# This code creates a dictionary for AROS.
# One can use it to check for duplicates (dictionary value > 1).

def AROcounter(file):
    d = {}
    for line in file:  
        if ">" in line:
            ARO = line.split('ARO:')[1]
            ARO = ARO.split('|')[0]
            if ARO not in d:
                d[ARO] = 1
            else:
                d[ARO] += 1 
            #if d[ARO] > 1:
            #   print(ARO)
    return d

# Example of how this function can be used.
'''
files = open("card_nucleotide.fasta", "r")

ds = AROcounter(files)

for ARO in ds:
    if ds[ARO] > 1:
        print(ARO)
'''