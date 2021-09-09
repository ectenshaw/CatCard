"""

#Basic scripts for running the GF FAFB project.
#copy and paste functions of interest into the python console


#Building the input set:

#imports necessary packages
import GFInputNeuronSet as NS
import subsetCreator as SC

#builds most basic set; we will call the GF input set "mySet"
mySet = NS.builder()

#order synapses - optional
mySet = SC.sortBySynL2H(mySet)



#Specific functions to add more data

#gets all node coordinate points of every neuron in set - don't run unless this info is necessary
#mySet.updateSkeletonNodes()

#returns and updates soma location
mySet.updateSomata()
#Find connectors for synapses
mySet.getConnectors()
#returns number of synapses received by various groups like LPLC2
mySet.getNumPartnersBySkid()
#returns total number of syns by branch for the group
mySet.getAllGFINSynByBranch()
#returns neuropil info for neurons
mySet.findNeuropils()
#finds branch synapse distributions
mySet.findBranchDistributions()
mySet.combineAllSynLocations()


----------------------------------------------------------
#Making CSV Files:
#Various save options when making a CSV file.
#Use the "makeCSV" functoin and change the format type for different data.
#Different formats were created based on the data we wanted to visualize


import exportToCSV as E2C
E2C.makeCSV(mySet, "saveGeneral")
E2C.makeCSV(mySet, "saveWithModality")

##File for the data tables!!
E2C.makeCSV(mySet, "saveWithAll")


----------------------------------------------------------
#Plot building:
import plotBuilder as PB
import runFigures as RF
import createPlots as CP

#run all figures discussed for paper
RF.runAllFigures(mySet)

#You can run plots individually by calling their functions in CP or PB
#allInfo is needed when viewing or interest in synapses on specific branches
allInfo = PB.getSynInfo(mySet)


"""