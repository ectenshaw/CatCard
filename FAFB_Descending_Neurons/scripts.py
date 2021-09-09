"""
Various scripts for the files in this package
"""

'''

Autoseg scripts

'''
'''
#creates the spreadsheets used in the DN Overview file of the DN_Autoseg folder
# making the DN files 

import DescendingNeuronSet as DNS
import checkV14
DNSet = DNS.builder()
checkV14.checkV14SKID(DNSet)
DNS.makeCSV(DNSet)


# making the AN files

import checkV14
import AscendingNeuronSet as ANS
ANSet = ANS.builder()
checkV14.checkV14SKID(ANSet)
ANS.makeCSV(ANSet)

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

#-----------------------------------------------------------
"""

DN Input Project Scripts

"""
'''
#DN/LC Gradients


#To create the LC gradient files
#Interested in the LC4 and LPLC2 gradients onto DNp01/02/04/11

import jsonNeurons as JN
import exportToCSV as e2c
import requests
import config
import json

token = config.token
auth = config.CatmaidApiTokenAuth(token)
project_id = config.project_id
import DNInputNeuronSet as NS


#Create the sets using SKID

myDNp01Set = NS.builder(4947529)
myDNp02Set = NS.builder(7138957)
myDNp04Set = NS.builder(6958818)
myDNp11Set = NS.builder(5349447)

#Create subsets for LC4

DNp01LC4 = NS.createGroupByAnnotation(myDNp01Set, 'putative LC4 neuron')
DNp02LC4 = NS.createGroupByAnnotation(myDNp02Set, 'putative LC4 neuron')
DNp04LC4 = NS.createGroupByAnnotation(myDNp04Set, 'putative LC4 neuron')
DNp11LC4 = NS.createGroupByAnnotation(myDNp11Set, 'putative LC4 neuron')

#Sort the neurons high to low

sorted01LC4 = NS.sortBySynH2L(DNp01LC4)
sorted02LC4 = NS.sortBySynH2L(DNp02LC4)
sorted04LC4 = NS.sortBySynH2L(DNp04LC4)
sorted11LC4 = NS.sortBySynH2L(DNp11LC4)

#Save the color gradient JSON (LC4)

JN.autoSaveJSONColorGrad(DNp01LC4)
JN.autoSaveJSONColorGrad(DNp04LC4)
JN.autoSaveJSONColorGrad(DNp02LC4)
JN.autoSaveJSONColorGrad(DNp11LC4)

-----

#Create subsets for LPLC2

DNp01LPLC2 = NS.createGroupByAnnotation(myDNp01Set, 'LPLC2')
DNp02LPLC2 = NS.createGroupByAnnotation(myDNp02Set, 'LPLC2')
DNp04LPLC2 = NS.createGroupByAnnotation(myDNp04Set, 'LPLC2')
DNp11LPLC2 = NS.createGroupByAnnotation(myDNp11Set, 'LPLC2')


#Sot the neurons high to low

sorted01LPLC2 = CN.sortBySynH2L(DNp01LPLC2)
sorted02LPLC2 = CN.sortBySynH2L(DNp02LPLC2)
sorted04LPLC2 = CN.sortBySynH2L(DNp04LPLC2)
sorted11LPLC2 = CN.sortBySynH2L(DNp11LPLC2)

#Save the color gradient JSON (LPLC2)

JN.autoSaveJSONColorGrad(DNp01LPLC2)
JN.autoSaveJSONColorGrad(DNp02LPLC2)
JN.autoSaveJSONColorGrad(DNp04LPLC2)
JN.autoSaveJSONColorGrad(DNp11LPLC2)

'''

'''
#Functions that produce json files for the LC for project Jinyong is working on. 

#Jinyong color scheem
LC4 = (0, 206, 209) #00ced1
DNp01 = (254, 95, 224) #fe5fe0
DNp02 = (255, 0, 0) #ff0000
DNp04 = (143, 57, 229) #8f39e5
DNp11 = (0, 0, 255) #0000ff


#-------------
#to run

import json
default_path = "/home/emily/Desktop/pyCharmOutputs"
import scripts as SCR

LC4List = [1319279, 873699, 1060322, 1325592, 873720, 1325197, 292337, 1060175, 1325528, 893079, 1325820, 858357, 
           1077484, 1324489, 2284700, 1108134, 874394, 1326615, 1077585, 309385, 1077372, 292771, 1325025, 3072214, 
           873664, 1075821, 1108155, 1060221, 872672, 285581, 1326385, 874312, 1325500, 308338, 284703, 310806, 
           1075777, 1325578, 1316949, 284788, 1075741, 1325636, 1325965, 867281, 1199415, 1060201, 2980141, 1325938, 
           867786, 2910014, 2909976, 874359, 1060195, 867557, 1326497]

SCR.makeLC4JSON(LC4List)
SCR.makeDNp01JSON()
SCR.makeDNp02JSON()
SCR.makeDNp04JSON()
SCR.makeDNp11JSON()

'''

import json
default_path = "/home/emily/Desktop/pyCharmOutputs"

#Uses a LIST of LC4 skeleton IDs

LC4List = [1319279, 873699, 1060322, 1325592, 873720, 1325197, 292337, 1060175, 1325528, 893079, 1325820, 858357,
           1077484, 1324489, 2284700, 1108134, 874394, 1326615, 1077585, 309385, 1077372, 292771, 1325025, 3072214,
           873664, 1075821, 1108155, 1060221, 872672, 285581, 1326385, 874312, 1325500, 308338, 284703, 310806,
           1075777, 1325578, 1316949, 284788, 1075741, 1325636, 1325965, 867281, 1199415, 1060201, 2980141, 1325938,
           867786, 2910014, 2909976, 874359, 1060195, 867557, 1326497]

def makeLC4JSON(LC4List):
    aListOfNeurons = []
    for item in LC4List:
        aNeuron = {
            "skeleton_id": item,
            "color": "#00ced1",
            "opacity": 1
        }
        aListOfNeurons.append(aNeuron)
    myJSON = json.dumps(aListOfNeurons, separators=(', \n', ': '))
    pathVar = str(default_path + "/LC4_Solo.json")
    c = open(pathVar, 'w')
    c.write(myJSON)
    c.close()
    return


def makeDNp01JSON(skid=4947529):
    aListOfNeurons = []
    aNeuron = {
        "skeleton_id": skid,
        "color": "#fe5fe0",
        "opacity": 1
    }
    aListOfNeurons.append(aNeuron)
    myJSON = json.dumps(aListOfNeurons, separators=(', \n', ': '))
    pathVar = str(default_path + "/DNp01_Solo.json")
    c = open(pathVar, 'w')
    c.write(myJSON)
    c.close()
    return


def makeDNp02JSON(skid=7138957):
    aListOfNeurons = []
    aNeuron = {
        "skeleton_id": skid,
        "color": "#ff0000",
        "opacity": 1
    }
    aListOfNeurons.append(aNeuron)
    myJSON = json.dumps(aListOfNeurons, separators=(', \n', ': '))
    pathVar = str(default_path + "/DNp02_Solo.json")
    c = open(pathVar, 'w')
    c.write(myJSON)
    c.close()
    return


def makeDNp04JSON(skid=6958818):
    aListOfNeurons = []
    aNeuron = {
        "skeleton_id": skid,
        "color": "#8f39e5",
        "opacity": 1
    }
    aListOfNeurons.append(aNeuron)
    myJSON = json.dumps(aListOfNeurons, separators=(', \n', ': '))
    pathVar = str(default_path + "/DNp04_Solo.json")
    c = open(pathVar, 'w')
    c.write(myJSON)
    c.close()
    return


def makeDNp11JSON(skid=5349447):
    aListOfNeurons = []
    aNeuron = {
        "skeleton_id": skid,
        "color": "#0000ff",
        "opacity": 1
    }
    aListOfNeurons.append(aNeuron)
    myJSON = json.dumps(aListOfNeurons, separators=(', \n', ': '))
    pathVar = str(default_path + "/DNp011_Solo.json")
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

