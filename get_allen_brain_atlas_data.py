#!/usr/bin/env python3

import requests
from allensdk.api.queries.rma_api import RmaApi
from pathlib import Path
from bs4 import BeautifulSoup

adult_human_urls = ['http://human.brain-map.org/api/v2/well_known_file_download/278447594', 
                    'http://human.brain-map.org/api/v2/well_known_file_download/278448166']

# sub-structures located in human frontal lobe
brain_structures = ['primary motor cortex (area M1, area 4)',
                    'dorsolateral prefrontal cortex',
                    'ventrolateral prefrontal cortex',
                    'anterior (rostral) cingulate (medial prefrontal) cortex',
                    'primary motor-sensory cortex (samples)']

structure_ids = []
dev_brain_donors = []
dev_brain_donor_ids = []
dev_gene_ids = {}

structure_id_str = ''

# Download RNA-seq data for 2 adult brains
for url in adult_human_urls:
    req = requests.get(url, stream=True, verify=False)
    filename = './data/' + url.split('/')[-1] + '.zip'
    
    print('Downloading... ' + url) 
    with open(filename, 'wb') as handle:
        for chunk in req.iter_content(chunk_size=512):
            if chunk:
                handle.write(chunk)


# Base class for Allen Brain Atlas API
rma = RmaApi()

# Get frontal lobe structure IDs
for structure in brain_structures:
    structure_query = rma.model_query('Structure',
                                      criteria="[name$il'{}']".format(structure),
                                      only=['structures.id'])
    structure_ids.append(str(structure_query[-1]['id']))

structure_id_str = ','.join(structure_ids)

#Retrieve all post-natal donors for developing brains

dev_brain_donors = rma.model_query('Donor',
                                   include="age[embryonic$eqfalse]",
                                   criteria="products[id$eq24]",
                                   only=['donors.id'])

for donor in dev_brain_donors:
    dev_brain_donor_ids.append(donor['id'])


dev_gid_outfile = Path('./data/dev_gene_ids.txt')

# Check if output file is already there
if not dev_gid_outfile.is_file():

# Retrieve all developing human brain gene ids 
    with open('./data/dev_genes.txt', 'r') as f, open('./data/dev_gene_ids.txt','w') as o:
        for gene in f:
            g = gene.strip('\n')

            try:

                temp_query = rma.model_query('Gene',
                                             criteria="[acronym$eq'"+ g +"'][type$eq'EnsemblGene'],organism[name$eq'Homo Sapiens']",
                                             only=['genes.id'])
                dev_gene_ids.update({g:temp_query[0]['id']})
                o.write(g + ',' + str(temp_query[0]['id']) + '\n')

            except Exception as e:

                dev_gene_ids.update({g:'!'})
                o.write(g + ',!\n')
                print(e)
                print(g)

# Load all gene ids if file already present
else:
    with open('./data/dev_gene_ids.txt', 'r') as f:
        for line in f:
            temp = line.strip('\n').split(',')
            dev_gene_ids.update({temp[0]:temp[1]})


# Retrieve all expression values for developing brain samples
for donor in dev_brain_donor_ids:

    with open ('./data/new_' + str(donor) + '.csv', 'w') as o:
        for gene in dev_gene_ids:

            if dev_gene_ids[gene] != '!':

                # Build API query
                query = "http://api.brain-map.org/api/v2/data/query.xml?criteria=service::" \
                        "dev_human_expression[set$eq'rna_seq_genes'][probes$eq{}][donors$eq{}]" \
                        "[structures$eq{}]"

                req = requests.get(query.format(dev_gene_ids[gene], donor, structure_id_str))

                soup = BeautifulSoup(req.content, 'xml')

                exp_values = soup.find_all('expression-level')
                print(exp_values)
                print(query.format(dev_gene_ids[gene], donor, structure_id_str)) 
                exp_values = exp_values[0].find_all('expression-level')

                id_counter = 0
                o.write(gene + ',')

                for value in exp_values:

                    if value and id_counter + 1 < len(exp_values):
                        o.write(value.get_text() + ',')

                    elif not value and id_counter + 1 < len(exp_values):
                        o.write('NA,')

                    elif value and id_counter + 1 == len(exp_values):
                        o.write(value.get_text() + '\n')

                    elif not value and id_counter + 1 == len(exp_values):
                        o.write('NA\n')

                    id_counter += 1



