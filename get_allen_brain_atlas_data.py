#!/usr/bin/env python3

import requests

dev_human_url = 'https://www.brainspan.org/api/v2/well_known_file_download/267666529'

adult_human_url = ''

req = requests.get(dev_human_url, stream=True, verify=False)
handle = open('dev_human.zip', 'wb')

for chunk in req.iter_content(chunk_size=512):
    if chunk:
        handle.write(chunk)
handle.close()


