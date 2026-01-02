# Phage Resistomes
This repository contains materials that I created for the analysis of tailed-bacteriophage resistomes.

Create local BLAST+ database:
###### Creates a nucliotide database:
```
makeblastdb -in card_nucleotide.fasta -dbtype nucl -out CARD_nucl
```
###### Creates a protein database:
```
makeblastdb -in card_proteins.fasta -dbtype prot -out CARD_prot
```
Run BLAST+ alignment:
###### For when you want to align a nucleotide query with a nucleotide database:
```
blastn -db CARD_nucl -query sequences.fasta -out results_nucleotide.out -outfmt 7
```
###### For when you want to align a nucleotide query with a protein database:
```
blastx -db CARD_prot -query sequences.fasta -out results_proteins.out -outfmt 7
```



>[!CAUTION]
>### Resources:
1. BLAST+ User Manual: https://www.ncbi.nlm.nih.gov/books/NBK569856/
