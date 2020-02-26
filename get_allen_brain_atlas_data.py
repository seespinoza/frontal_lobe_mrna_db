#!/usr/bin/env python3

import requests

# URL for developing human RNA-seq data
dev_human_url = 'https://www.brainspan.org/api/v2/well_known_file_download/267666529'

# URLs for adult human RNA-seq data
adult_human_url1 = 'http://human.brain-map.org/api/v2/well_known_file_download/278447594'

adult_human_url2 = 'http://human.brain-map.org/api/v2/well_known_file_download/278447594'


req = requests.get(dev_human_url, stream=True, verify=False)
handle = open('./data/dev_human.zip', 'wb')

# download dev_human_url as .zip file
for chunk in req.iter_content(chunk_size=512):
    if chunk:
        handle.write(chunk)
handle.close()

req = requests.get(adult_human_url1, stream=True, verify=False)
handle1 = open('./data/adult_human1.zip', 'wb')

# download adult_human_url1 as .zip file
for chunk in req.iter_content(chunk_size=512):
    if chunk:
        handle1.write(chunk)
handle1.close()


req = requests.get(adult_human_url2, stream=True, verify=False)
handle2 = open('./data/adult_human2.zip', 'wb')

#downlaod adult_human_url2 as .zip file
for chunk in req.iter_content(chunk_size=512):
    if chunk:
        handle2.write(chunk)
handle2.close()
