# Phage Resistomes
This repository contains materials that I created for the analysis of tailed-bacteriophage resistomes.

Create local BLAST+ database:
```
makeblastdb -in card_nucleotide.fasta -dbtype nucl -out CARD_nucl
makeblastdb -in card_proteins.fasta -dbtype prot -out CARD_prot
```

>[!CAUTION]
>### Resources:
1. BLAST+ User Manual
https://www.ncbi.nlm.nih.gov/books/NBK569856/
