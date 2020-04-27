#!/usr/bin/env python3

adult_matrix = open('./data/adult_values.txt', 'r')
dev_matrix = open('./data/dev_values.txt', 'r')

adult_genes = []
dev_genes = []
merged_genes =[]

adult_dict = {}
dev_dict = {}
# get a list of genes shared by both samples
counter = 0

for line in adult_matrix:
    if counter != 0:
        adult_genes.append(line.split(',')[0])
    counter += 1

for line in dev_matrix:
    
    if counter != 0:
        gene = line.split(',')[0]
        
        if gene in adult_genes:
            merged_genes.append(gene)

    counter += 1


# Create dictionaries

adult_matrix.seek(0)
counter = 0 

for line in adult_matrix:
    if counter == 0:
        temp_line = line.strip('\n').split(',')[1:]
        adult_dict[-1] = temp_line
    else:
        temp_line = line.strip('\n').split(',')

        if temp_line[0] in merged_genes:
            
            adult_dict[temp_line[0]] = temp_line[1:]
    counter += 1


dev_matrix.seek(0)
counter = 0
for line in dev_matrix:
    if counter == 0:
        temp_line = line.strip('\n').split(',')[1:28]
        dev_dict[-1] = temp_line
    else:
        temp_line = line.strip('\n').split(',')

        if temp_line[0] in merged_genes:
            dev_dict[temp_line[0]] = temp_line[1:28]
    counter += 1


# Created merged matrix
with open('./data/merged_values.txt', 'w') as m:
    m.write('Genes,' + ','.join(adult_dict[-1]) + ',' + ','.join(dev_dict[-1]) + '\n')
    
    for gene in merged_genes:
        m.write(gene + ',' + ','.join(adult_dict[gene]) + ',' + ','.join(dev_dict[gene]) + '\n')
