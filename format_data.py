#!/usr/bin/env python3
import os

brain_structures = ['dorsolateral prefrontal cortex',
                    'ventrolateral prefrontal cortex',
                    'anterior (rostral) cingulate (medial prefrontal) cortex',
                    'primary motor-sensory cortex (samples)',
                    'primary motor cortex (area M1, area 4)']


directory = './data/'

counter = 0

def write_exp_val_tab(p, f, s):
    patient = filename.split('.')[0]

    with open(p, 'r') as f, open('./data/' + patient + '.tsv', 'w') as o:
        for line in f:
            line_temp = line.strip('\n').split(',')

            o.write(patient + '\t')
            o.write(line_temp[0] + '\t')
            o.write(brain_structures[s] + '\t')
            o.write(line_temp[-1])



# Format data for expression_values
for f in os.listdir(directory):
    filename = os.fsdecode(f)
    
    print(filename)
    if f.endswith('.csv'):
        path = os.path.join(directory, filename)

        write_exp_val_tab(path, filename, counter)
        counter += 1

# Format data for differentially_expressed_genes



