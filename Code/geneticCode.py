"""
@author: Nadia Lenskaia 2026
All rights reserved.
"""
# This code takes a nucleotide sequence and translates it into a protein sequence using genetic code 11
# https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?mode

seq = "TTGAATTCTATCAAAAAAATA"


AAs  =   "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
Starts = "---M------**--*----M------------MMMM---------------M------------"
Base1  = "TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG"
Base2  = "TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG"
Base3  = "TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG"

n = len(AAs)
d = {}

#for ch in AAs:
for i in range(n):
    codon = Base1[i] + Base2[i] + Base3[i]
    if codon not in d:
        d[codon] = AAs[i]

left = ""

if len(seq) % 3 != 0:
    remaind = len(seq) % 3
    lastoneortwo = len(seq)-remaind
    left = seq[lastoneortwo:]

    
m = len(seq) // 3
mm = range(m)


AAseq = ""


for num in mm:
    cod = seq[0+3*num:3+3*num]
    AAseq += d[cod]
    #print(cod, d[cod])
print(AAseq, left)




    
