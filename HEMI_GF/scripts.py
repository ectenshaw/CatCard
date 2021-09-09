"""
#scripts

#Turns CSV file into a set like the FAFB GF data

import GFInputFunctions as GFF
import Hemi_GFInputNeuronSet as HNS

GFInputNeurons = GFF.readCSV()

#pulls relevant body IDs and GF input type
bodyDict, classDict, somaHemisphere = GFF.getInputBodiesAndType(GFInputNeurons)

#puts body IDs into query
queryResults = GFF.gfInputQuery(bodyDict)

#add GF types to data
queryResults = GFF.addInputType(bodyDict, queryResults, somaHemisphere)


queryArray = GFF.queryDataFrameToArray(queryResults)
inputList = GFF.queryArrayToNeuronList(queryArray)
inputSet = HNS.builder(inputList)


ex: how to find specific dataframe entry
queryResults.loc[queryResults['input.bodyId'] == 2063767972]

"""


''' 
GF LC4 connectivity 
Results in CSV of LC4/GF connections
To Run:
LC4 -> GF synapes example:

import GF_LC4_Syns as GLC

queryResults = GLC.getTypeCoords("LC4", 2307027729)
GLC.getPostsynPartners(queryResults, "LC4Syns.csv")
queryResults2 = GLC.getTypeCoords2("LC4", 2307027729)
GLC.getPostsynPartners2(queryResults2, "LC4Syns2.csv")
'''


'''
#example of hop queries in GF_Input_Hops
import GF_Input_Hops as GFIH

GFIH.ROITwoHop("AB")  #replace with any ROI
GFIH.GFInputConnect()
GFIH.allROIInputs()
GFIH.interneuronQuery('TYPE')
GFIH.getMBOneHop()

'''