#!/usr/bin/env python3
import os

brain_structures = ['dorsolateral prefrontal cortex',
                    'ventrolateral prefrontal cortex',
                    'anterior (rostral) cingulate (medial prefrontal) cortex',
                    'primary motor-sensory cortex (samples)',
                    'primary motor cortex (area M1, area 4)']

expr_values = []

outfile = open('./data/dev.tsv', 'w')

counter = 0


# Converts csv file to tsv file for sql database
def write_exp_val_tab(p, f, s, o):
    patient = filename.split('.')[0].split('_')[1]

    temp_expr_dict = {}
    with open(p, 'r') as f:
        for line in f:
            line_temp = line.strip('\n').split(',')

            o.write(patient + '\t')
            o.write(line_temp[0] + '\t')
            o.write(brain_structures[s] + '\t')
            o.write(line_temp[-1] + '\n')
            
            if not line_temp[-1]:
                temp_expr_dict[line_temp[0]] = 'NA'
            else:
                temp_expr_dict[line_temp[0]] = line_temp[-1]

        temp_expr_dict[-1] = patient
        expr_values.append(temp_expr_dict)



# Format data for expression_values
for f in os.listdir('./data'):
    filename = os.fsdecode(f)
    
    
    if f.endswith('.csv'):

        print(filename)
        path = os.path.join('./data', filename)

        write_exp_val_tab(path, filename, counter, outfile)
        counter += 1

        if counter == 5:
            counter = 0

# Format data for differentially_expressed_genes

outfile.close()

# Write out data in dictionary as expression matrix

header = [sample[-1] for sample in expr_values]

with open('./data/dev_values.txt', 'w') as x:

    x.write(',' + ','.join(header) + '\n')

    for gene in expr_values[0]:

        if gene != -1:
            temp_values = [val[gene] for val in expr_values]
            
            x.write(gene + ',')
            x.write(','.join(temp_values) + '\n')

    

