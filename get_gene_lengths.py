#!/usr/bin/env python3
from Bio import Entrez

Entrez.email = 'sespinoza@unomaha.edu'
handle = Entrez.esearch(db='nucleotide', retmax=10, term='MLL5[Gene Name] AND Homo sapiens[Organism]', idtype='acc')

record = Entrez.read(handle)['IdList']
handle.close()

print(record)
