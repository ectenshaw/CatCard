"""
Emily Tenshaw
CAT-Card
12/2/2020

This file looks at the SKID of neurons in autoseg and checks to see if they are in V14 of FAFB.
"""

import config
import requests
import json

token = config.token
auth = config.CatmaidApiTokenAuth(token)

project_id = config.project_id


'''
Checks V14 catmaid site and compares SKID numbers with the autoseg DNs/ANs
It adds the annotation "Exists V14" to any neuron SKID that exists in V14
'''


def checkV14SKID(neuronSet):
    skids = []
    v14skids = []
    for i in neuronSet:
        if i not in skids:
            skids.append(i.skeletonID)
    for skid in skids:
        response = requests.get(
            'https://neuropil.janelia.org/tracing/fafb/v14/{}/skeletons/{}/root'.format(project_id, skid),
            auth=auth  # ,
        )
        if response.status_code == 200:
            v14skids.append(skid)

    for i in neuronSet:
        if i.skeletonID in v14skids:
            i.existV14 = "True"

    for i in neuronSet:
        skid = i.skeletonID
        skid = int(float(skid))
        if i.existV14 is "True":
            if "Exists V14" not in i.annotations:
                addAnnotation(skid, "Exists V14")
    return


'''
Adds an annotation to the autoseg catmaid site
'''


def addAnnotation(neuron, newAnnotation, addToSkeletons=True):
    if addToSkeletons is True:
        mySkids = [neuron]

        response = requests.post(
            'https://neuropil.janelia.org/tracing/fafb/v14-seg-li-190805.0/{}/annotations/add'.format(project_id),
            auth=config.CatmaidApiTokenAuth(token),
            data={'skeleton_ids': mySkids, 'annotations': newAnnotation}
        )

    myResults = json.loads(response.content)
    print(myResults)
    return
