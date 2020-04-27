#!/usr/bin/env python3
import pandas as pd
import numpy as np

# Read in meta data columns
adult1_annot = pd.read_csv('./data/adult_patient1/SampleAnnot.csv')
adult2_annot = pd.read_csv('./data/adult_patient2/SampleAnnot.csv')

# Read in raw counts
adult1_counts = pd.read_csv('./data/adult_patient1/RNAseqCounts.csv', header=None)
adult2_counts = pd.read_csv('./data/adult_patient2/RNAseqCounts.csv', header=None)

# Read in Gene info
adult1_genes = pd.read_csv('./data/adult_patient1/Genes.csv')
adult2_genes = pd.read_csv('./data/adult_patient2/Genes.csv')

# Insert row numbers to annotations
adult1_annot.insert(0, 'row_id', range(1, 122))
adult2_annot.insert(0, 'row_id', range(1, 122))

# Retrieve all of the Frontal Lobe samples only
adult1_annot = adult1_annot[adult1_annot.main_structure == 'FL']
adult2_annot = adult2_annot[adult2_annot.main_structure == 'FL']

# Save the sample names and brain sub structures
adult1_annot_dict = adult1_annot[['row_id','sample_name', 'sub_structure']].to_dict()
adult2_annot_dict = adult2_annot[['row_id','sample_name', 'sub_structure']].to_dict()

adult1_counts_list = adult1_counts.to_numpy()
adult2_counts_list = adult2_counts.to_numpy()

adult1_trans_len = adult1_genes['median_transcriptome_length'].to_numpy()
adult2_trans_len = adult2_genes['median_transcriptome_length'].to_numpy()

# Get all row ids in list
c1 = list(adult1_annot_dict['row_id'].values())
c2 = list(adult2_annot_dict['row_id'].values())


with open('./data/adult1.tsv', 'w') as t:

    expr_values = []
    for column in c1:

        # per million scaling factor for RPKM
        mil_factor = adult1_counts.iloc[:, column].sum() / 1000000
        counter = 0
        
        sample = adult1_annot_dict['sample_name'][column - 1]
        temp = [sample]

        for gene in adult1_counts_list:

            rpkm = gene[column] / adult1_trans_len[counter]
            t.write(sample + '\t')
            t.write(gene[0] + '\t')
            t.write(adult1_annot_dict['sub_structure'][column - 1] + '\t')
            t.write(str(rpkm) + '\n')

            temp.append(rpkm)

            counter += 1

        expr_values.append(temp)


with open('./data/adult2.tsv', 'w') as t:

    for column in c2:

        # per million scaling factor for RPKM
        mil_factor = adult2_counts.iloc[:, column].sum() / 1000000
        counter = 0

        sample = adult2_annot_dict['sample_name'][column - 1]
        temp = [sample]

        for gene in adult2_counts_list:

            rpkm = gene[column] / adult2_trans_len[counter]
            t.write(sample + '\t')
            t.write(gene[0] + '\t')
            t.write(adult2_annot_dict['sub_structure'][column - 1] + '\t')
            t.write(str(rpkm) + '\n')

            temp.append(rpkm)

            counter += 1

        expr_values.append(temp)




# Write out expression values in matrix
header = [sample[0] for sample in expr_values]

gene_list = adult1_genes['gene_symbol'].to_numpy()

with open('./data/adult_values.txt', 'w') as x:

    x.write(',' + ','.join(header) + '\n')
    counter = 0
    for value in expr_values[0]:
            
        if counter > 0:
            temp = [str(i[counter]) for i in expr_values]

            x.write(gene_list[counter - 1] + ',' + ','.join(temp) + '\n')

        counter += 1


