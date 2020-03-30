#!/usr/bin/env python3

import requests

# download current go.obo file
go_obo_url = 'http://current.geneontology.org/ontology/go.obo'

req = requests.get(go_obo_url, stream=True, verify=False)
handle = open('./data/go.obo', 'wb')

for chunk in req.iter_content(chunk=512):
    if chunk:
        handle.write(chunk)
handle.close()

