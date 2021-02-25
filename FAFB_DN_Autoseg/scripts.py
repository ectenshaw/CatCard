"""
Various scripts for the files in this package
"""

'''
# making the DN files 

import DnAutosegClassSet as DNCS
import checkV14
DNSet = DNCS.builder()
checkV14.checkV14SKID(DNSet)
DNCS.makeCSV(DNSet)


# making the AN files

import checkV14
import AscendingNeuronClassSet as ANCS
ANSet = ANCS.builder()
checkV14.checkV14SKID(ANSet)
ANCS.makeCSV(ANSet)

# making plots

import makePlots as MP
DN_DF = MP.openDN_CSV()
MP.makeSunburstCharts(DN_DF)
MP.onlyFindSoma(DN_DF)
MP.identifiedDNs(DN_DF)


#to get neurons to import
tagged = []
for i in DNSet:
    if "Exists V14" not in i.annotations:
        if "ID To Import" in i.annotations:
            tagged.append(i.skeletonID)

listOfTen = tagged[0:10]

import json

aListOfNeurons = []
for item in listOfTen:
    aNeuron = {
    "skeleton_id": item,
    "color": "#00eee5",
    "opacity": 1
    }
    aListOfNeurons.append(aNeuron)
    
myJSON = json.dumps(aListOfNeurons, separators=(', \n', ': '))



pathVar = "/home/emily/Desktop/pyCharmOutputs/DN_Import/toImport.json"
myFile = str(pathVar)

c = open(myFile, 'w')
c.write(myJSON)
c.close()
'''
