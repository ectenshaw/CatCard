#import MyCustomDNNeuronClass as  DNC
#import GetDNrightConnectivity as GDC
# myList =GDC.removeExtra(7138957)
# test = list(myList.keys())
# myCells = DNC.buildFromSkidList(test)
# myCells = DNC.builder(7138957)
import jsonNeurons as JN
import exportToCSV as e2c
import requests
import config
import json

token = config.token
auth = config.CatmaidApiTokenAuth(token)
project_id = config.project_id


import DNInputNeuronSet as NS

myDNp10Set = NS.builder(5279996)




myDNp01Set = NS.builder(4947529)
# print(myDNp01Set)
DNp01LC4 = NS.createGroupByAnnotation(myDNp01Set, 'putative LC4 neuron')
sorted01LC4 = NS.sortBySynH2L(DNp01LC4)
#DNp01LPLC2 = CN.createGroupByAnnotation(myDNp01Set, 'LPLC2')
# e2c.makeCSV(myDNp01Set, 'saveGeneralSpecificAnnotations')

myDNp02Set = NS.builder(7138957)
# print(myDNp02Set)
DNp02LC4 = NS.createGroupByAnnotation(myDNp02Set, 'putative LC4 neuron')
sorted02LC4 = NS.sortBySynH2L(DNp02LC4)
#DNp02LPLC2 = CN.createGroupByAnnotation(myDNp02Set, 'LPLC2')
# e2c.makeCSV(myDNp02Set, 'saveGeneralSpecificAnnotations')

myDNp04Set = NS.builder(6958818)
DNp04LC4 = NS.createGroupByAnnotation(myDNp04Set, 'putative LC4 neuron')
#DNp04LPLC2 = CN.createGroupByAnnotation(myDNp04Set, 'LPLC2')
sorted04LC4 = NS.sortBySynH2L(DNp04LC4)
#sorted04LPLC2 = CN.sortBySynH2L(DNp04LPLC2)

# e2c.makeCSV(myDNp04Set, 'saveGeneralSpecificAnnotations')

myDNp11Set = NS.builder(5349447)
# print(myDNp02Set)
DNp11LC4 = NS.createGroupByAnnotation(myDNp11Set, 'putative LC4 neuron')
sorted11LC4 = NS.sortBySynH2L(DNp11LC4)

JN.autoSaveJSONColorGrad(DNp01LC4)

JN.autoSaveJSONColorGrad(DNp04LC4)

#JN.autoSaveJSONColorGrad(DNp04LPLC2)

JN.autoSaveJSONColorGrad(DNp02LC4)

JN.autoSaveJSONColorGrad(DNp11LC4)

sorted01LC4.colorByGradient()
sorted02LC4.colorByGradient()
sorted04LC4.colorByGradient()
sorted11LC4.colorByGradient()





'''
#Jinyong color scheem
LC4 = (0, 206, 209) #00ced1
DNp01 = (254, 95, 224) #fe5fe0
DNp02 = (255, 0, 0) #ff0000
DNp04 = (143, 57, 229) #8f39e5
DNp11 = (0, 0, 255) #0000ff
'''


def makeLC4JSON(mySet):
    aListOfNeurons = []
    for item in mySet:
        aNeuron = {
            "skeleton_id": item.skeletonID,
            "color": "#00ced1",
            "opacity": 1
        }
        aListOfNeurons.append(aNeuron)
    myJSON = json.dumps(aListOfNeurons, separators=(', \n', ': '))
    pathVar = "/home/emily/Desktop/pyCharmOutputs/LC4_Solo.json"
    c = open(pathVar, 'w')
    c.write(myJSON)
    c.close()
    return




def makeDNp01JSON(skid = 4947529):
    aListOfNeurons = []
    aNeuron = {
        "skeleton_id": skid,
        "color": "#fe5fe0",
        "opacity": 1
    }
    aListOfNeurons.append(aNeuron)
    myJSON = json.dumps(aListOfNeurons, separators=(', \n', ': '))
    pathVar = "/home/emily/Desktop/pyCharmOutputs/DNp01_Solo.json"
    c = open(pathVar, 'w')
    c.write(myJSON)
    c.close()
    return

def makeDNp02JSON(skid = 7138957):
    aListOfNeurons = []
    aNeuron = {
        "skeleton_id": skid,
        "color": "#ff0000",
        "opacity": 1
    }
    aListOfNeurons.append(aNeuron)
    myJSON = json.dumps(aListOfNeurons, separators=(', \n', ': '))
    pathVar = "/home/emily/Desktop/pyCharmOutputs/DNp02_Solo.json"
    c = open(pathVar, 'w')
    c.write(myJSON)
    c.close()
    return

def makeDNp04JSON(skid = 6958818):
    aListOfNeurons = []
    aNeuron = {
        "skeleton_id": skid,
        "color": "#8f39e5",
        "opacity": 1
    }
    aListOfNeurons.append(aNeuron)
    myJSON = json.dumps(aListOfNeurons, separators=(', \n', ': '))
    pathVar = "/home/emily/Desktop/pyCharmOutputs/DNp04_Solo.json"
    c = open(pathVar, 'w')
    c.write(myJSON)
    c.close()
    return

def makeDNp11JSON(skid = 5349447):
    aListOfNeurons = []
    aNeuron = {
        "skeleton_id": skid,
        "color": "#0000ff",
        "opacity": 1
    }
    aListOfNeurons.append(aNeuron)
    myJSON = json.dumps(aListOfNeurons, separators=(', \n', ': '))
    pathVar = "/home/emily/Desktop/pyCharmOutputs/DNp11_Solo.json"
    c = open(pathVar, 'w')
    c.write(myJSON)
    c.close()
    return








def makeJson(mySet):
    aListOfNeurons = []
    for item in mySet:
        mySKID = item.skeletonID
        aNeuron = {
            "skeleton_id": mySKID,
            "color": "#00eee5",
            "opacity": 1
        }
        aListOfNeurons.append(aNeuron)

    myJSON = json.dumps(aListOfNeurons, separators=(', \n', ': '))
    return myJSON

"""

e2c.makeCSV(sorted01LC4, 'saveSKIDwithColor')
e2c.makeCSV(sorted02LC4, 'saveSKIDwithColor')
e2c.makeCSV(sorted04LC4, 'saveSKIDwithColor')
e2c.makeCSV(sorted11LC4, 'saveSKIDwithColor')

#CSVs for interactive 3D graph
e2c.makeCSV(DNp02LC4, "saveSKIDwithXYZandColor")
e2c.makeCSV(DNp04LC4, "saveSKIDwithXYZandColor")
e2c.makeCSV(DNp11LC4, "saveSKIDwithXYZandColor")

DNp11LPLC2 = CN.createGroupByAnnotation(myDNp11Set, 'LPLC2')

DNp10InputNeurons = CN.builder(5279996)
oldClusterEntityIDs = []
newClusterSkeletonIDs = []
# cluster3 == 8900927
# cluster4 == 8758377
# entity_id == neuron id
# skeletonID = skid

for item in DNp10InputNeurons:
    if 'DNp10_Input_Cluster3' in item.annotations:
        newClusterSkeletonIDs.append(item.skeletonID)

        '''oldClusterEntityIDs.append(item.skeletonID + 1)

        responseOne = requests.post(
            'https://neuropil.janelia.org/tracing/fafb/v14/{}/annotations/remove'.format(project_id),
            auth=config.CatmaidApiTokenAuth(token),
            data={'entity_ids': oldClusterEntityIDs, 'annotation_ids': [8758377]}
        )
        responseOne = json.loads(responseOne.content)
        print(responseOne)'''

        responseTwo = requests.post(
            'https://neuropil.janelia.org/tracing/fafb/v14/{}/annotations/add'.format(project_id),
            auth=config.CatmaidApiTokenAuth(token),
            data={'skeleton_ids[0]': newClusterSkeletonIDs, 'annotations': [8900927]}
        )

        responseTwo = json.loads(responseTwo.content)
        print(responseTwo)

# getDNp020411 DNp02 = 7138957 DNp04 = 6958818 DNp11=5349447

myDNp02Set = CN.builder(7138957)
# print(myDNp02Set)
DNp02LC4 = CN.createGroupByAnnotation(myDNp02Set, 'putative LC4 neuron')
sorted02LC4 = CN.sortBySynH2L(DNp02LC4)
import exportToCSV as e2c

e2c.makeCSV(sorted02LC4, formatType='saveDNp020411')

# if e2c doesn't work try the below

import GetDNrightConnectivity as GC
myInfo = sorted02LC4.getConnectors()
def fNew(i, conList):
    mytest = list(conList[i][6].keys())
    return mytest
formatTypeDict = 'saveDNp020411'
mySet = sorted02LC4
formatType = 'saveDNp020411'
import os
import csv
import datetime
now = datetime.datetime.now()
neuronNames = {}
DNs = [7138957,6958818,5349447]
for neuron in mySet:
    neuronNames[str(neuron.skeletonID)] = neuron.neuronName
cleanedInfo = {}
for item in myInfo:
    mytest = fNew(item, myInfo)
    if 7138957 in mytest or 6958818 in mytest or 5349447 in mytest:
        cleanedInfo[item] = myInfo[item]
with open(myFile, 'w', newline = '') as outfile:
    myWriter = csv.writer(outfile)
    myWriter.writerow(['connector_id', 'X', 'Y', 'Z', 'NeuronName', 'skeletonID', 'DNp02', 'DNp04', 'DNp11'])
    for con in cleanedInfo:
        aName = str(cleanedInfo[con][0])
        for abc in DNs:
            if abc in cleanedInfo[con][6].keys():
                cleanedInfo[con].append(True)
            else:
                cleanedInfo[con].append(False)
        myWriter.writerow([cleanedInfo[con][1], cleanedInfo[con][2], cleanedInfo[con][3], cleanedInfo[con][4], neuronNames[aName], cleanedInfo[con][0], cleanedInfo[con][7], cleanedInfo[con][8], cleanedInfo[con][9]])


# print(myCells)
LC6DN_1 = CN.builder(2439409)
LC6DN_2 = CN.builder(277739)

LC6DN_1_filtered = CN.createGroupByAnnotation(LC6DN_1, 'LC6 neuron')
LC6DN_2_filtered = CN.createGroupByAnnotation(LC6DN_2, 'LC6 neuron')
"""