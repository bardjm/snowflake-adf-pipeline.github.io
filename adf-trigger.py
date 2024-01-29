#!/usr/bin/env python
# coding: utf-8

# In[18]:


import requests
import json
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


url = 'https://api.euw.kiko.test.eva-online.cloud/message/ListStations'
 
headers = {'Authorization': 'Bearer DC61C042CB33A93DF69273675F63D542E02B427136791851427FF7F8AC869DA6', 'eva-user-agent':'Streamline', 'Content-Type': 'application/json'}


for x in range(0, 200, 50):

    body_data = {
        "PageConfig": {
            "Filter": {
                "TypeID": 1
            } ,
            "Start":x,
            "Limit":50
        }
    }

    req = requests.post(url, headers=headers, json=body_data)
    
    connect_str = 'DefaultEndpointsProtocol=https;AccountName=streamlinedevapistorage;AccountKey=dPM/k0EulMQtf589LnCHaZOMOW9sBVvG6lbO+foXFTssDA4Ajy0qfJdemjgrnUnh8vsL2pbUpJor+AStuAXZFA==;EndpointSuffix=core.windows.net'
    
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    
    container_name = "api-response-data"
    
    file_name = "watchtower-stations-" + str(x+1) +  ".json"
    
    container_client = blob_service_client.get_container_client(container_name)
    
    blob_client = blob_service_client.get_blob_client(container_name, file_name)
    
    blob_client.upload_blob(req.text, blob_type="BlockBlob")
    
    #file_name= "/Users/jyoti.bardhanstreamlinedigital.com/Downloads/meraki-stations-" + str(x+1) +  ".json"

    #with open(file_name, "w") as outfile:
        #json.dump(req.text, outfile)

