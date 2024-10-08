import requests
import json
import getAllVolumeIDs as gAVI
import config

token = config.token
auth = config.CatmaidApiTokenAuth(token)
project_id = config.project_id


# gets list of all info about a skid
def getSkelInfo():
    # mySkids = GAREI.getListOfSkID_int()

    # mySkid=str(mySkids[0])
    mySkid = 4947529

    response = requests.post(
        'https://neuropil.janelia.org/tracing/fafb/v14/{}/skeletons/compact-detail'.format(project_id),
        auth=auth,
        data={'skeleton_ids': mySkid}
    )

    skelInfo = json.loads(response.content)
    myD = skelInfo['skeletons']
    newList = []

    for i in myD:
        for e in myD[i]:
            for x in e:
                newList.append(x)

    return newList


def getNodeCoordinates():
    myInfo = getSkelInfo()
    myNodes = []
    for i in myInfo:
        tempCoor = i[3:6]
        myNodes.append(tempCoor)

    return myNodes


# Please provide valid X, Y, and Z coordinates - What is type number? Not float?
def getIntersection():
    mySkel = getNodeCoordinates()
    myVols = gAVI.getVolumeIDintList()
    intersectingVolumes = []
    for i in myVols:
        # print(i)
        volume_id = i
        for e in mySkel:
            x = e[0]
            y = e[1]
            z = e[2]
            payload = {'x': x, 'y': y, 'z': z}
            b = requests.get(
                'https://neuropil.janelia.org/tracing/fafb/v14/{}/volumes/{}/intersect'.format(project_id, volume_id),
                auth=auth,
                params=payload
            )
            # print(b.content)
            a = json.loads(b.content)
            if a['intersects'] == True:
                intersectingVolumes.append(i)
                break

            # print(response)
    return intersectingVolumes


def GetIntersectionName():
    volDict = gAVI.getVolumeIDs()
    print("volDict", volDict)
    volName = []
    for i in a:
        volName.append(volDict[a])
    print("volName", volName)
    return volName


# def getNodesBySkIDandAnnotation(nodeSet, tag):
# treenode_ids[0]: 9730168
# skid: ["tag"]
# labels: true

# tag = str(tag)
# response = requests.post(
#       'https://neuropil.janelia.org/tracing/fafb/v14/{}/skeleton/find_labels'.format(project_id),
#        auth = auth,
#         data = {label_regex : 'tag', x = nodeSet[i], y}
#  )

# myNode = json.loads(response.content)
# myD = skelInfo['skeletons']
# newList = []

# for i in myD:
#   for e in myD[i]:
#      for x in e:
#         newList.append(x)

# return myNode


# for i in mySkids:
#   mySkid = str(i)

#  response = requests.post(
#         'https://neuropil.janelia.org/tracing/fafb/v14/{}/skeletons/compact-detail'.format(project_id),
#        auth = auth,
#       data = {'skeleton_ids' : mySkid}
# )

# skelInfo = json.loads(response.content)
# return skelInfo
# myDict = skelInfo['skeletons']

# input should be an array of skeleton id integers
def getSkelNodesWithSomaTags(myNeuronList):
    mySkids = []
    for item in myNeuronList:
        mySkids.append(item.skeletonID)

    response = requests.post(
        'https://neuropil.janelia.org/tracing/fafb/v14/1/skeletons/compact_skeleton_detail_many',
        auth=auth,
        data={'skeleton_ids': mySkids, 'with_tags': 'true'}
    )

    skelInfo = json.loads(response.content)
    # myD = skelInfo['skeletons']
    # newList = []

    # for i in myD:
    #   for e in myD[i]:
    #      for x in e:
    #         newList.append(x)

    return skelInfo


def GetSkelInfoWithTags(myNeurons):
    # mySkids = []
    # for item in myNeuronList:
    #   mySkids.append(item.skeletonID)
    # mySkids = GAREI.getListOfSkID_int()

    # mySkid=str(mySkids[0])
    # mySkid = 4947529
    response = requests.post(
        'https://neuropil.janelia.org/tracing/fafb/v14/{}/skeletons/compact-detail'.format(project_id),
        auth=auth,
        data={'skeleton_ids': myNeurons[0].skeletonID, 'with_tags': 'soma'}
    )

    skelInfo = json.loads(response.content)
    # myD = skelInfo['skeletons']
    # newList = []

    # for i in myD:
    #   for e in myD[i]:
    #      for x in e:
    #         newList.append(x)

    return skelInfo


# input is a single object of type myCustomDNNeuron, output is a list of floats representing the x,y, and z coordinate of the soma in catmaid.
def getSoma(myNeur):
    skeletonID = myNeur.skeletonID
    response = requests.get(
        'https://neuropil.janelia.org/tracing/fafb/v14/1/skeletons/{}/node-overview'.format(skeletonID),
    )
    myDict = json.loads(response.content)
    somaAndCoordinates = [None] * 3
    a = None
    for i in myDict[2]:
        # print(i)
        if 'soma' in i:
            a = i[0]
            # print(i)
    for item in myDict[0]:
        if a is None:
            print(myNeur, 'has no soma')
            break  # break might break this code consider removing if it stops working
        elif a in item:
            somaAndCoordinates[0] = item[3]
            somaAndCoordinates[1] = item[4]
            somaAndCoordinates[2] = item[5]
    # somaAndCoordinates[myNeur.skeletonID] = z
    return somaAndCoordinates


# attempted fix of above
'''#input is a single object of type myCustomDNNeuron, output is a list of integers representing the x,y, and z coordinate of the soma in catmaid. BUG: Cannot find somata of all LPLC2 - fix this
def getSoma(myNeur):
    skeletonID = myNeur.skeletonID
    response = requests.get(
            'https://neuropil.janelia.org/tracing/fafb/v14/1/skeletons/{}/node-overview'.format(skeletonID), 
    )
    myDict = json.loads(response.content)
    somaAndCoordinates = [None] * 3
    #print(len(myDict))
    for i in myDict[2]:
        if 'soma' in i:
            a = i[0]
    for i in myDict[0]:
        if a not in locals():
            print("{} does not have a soma".format(skeletonID))
            break
        elif a in i:
            somaAndCoordinates[0] = i[3]
            somaAndCoordinates[1] = i[4]
            somaAndCoordinates[2] = i[5]
    #somaAndCoordinates[myNeur.skeletonID] = z
    return somaAndCoordinates'''


# currently unused dictionary version of the above, wherein the result returned is a dictionary with key = skid and values are ordered xyz coordinates
# input is a single object of type myCustomDNNeuron, output is a list of integers representing the x,y, and z coordinate of the soma in catmaid. if desired soma node number can be returned by changing line 200 to ... = [x, z]
def getSkidSomaDict(myNeur):
    skeletonID = myNeur.skeletonID
    response = requests.get(
        'https://neuropil.janelia.org/tracing/fafb/v14/1/skeletons/{}/node-overview'.format(skeletonID),
    )
    myDict = json.loads(response.content)
    somaAndCoordinates = {}
    for i in myDict[2]:
        if 'soma' in i:
            a = i[0]
    for i in myDict[0]:
        if a in i:
            somaAndCoordinates['x'] = i[3]
            somaAndCoordinates['y'] = i[4]
            somaAndCoordinates['z'] = i[5]
    # somaAndCoordinates[myNeur.skeletonID] = z
    return somaAndCoordinates


# input is DN input neuron, output is a list containing lists of each node coordinate point
def getAllNodes(myNeuron):
    mySkid = myNeuron.skeletonID
    # mySkids = GAREI.getListOfSkID_int()

    # mySkid=str(mySkids[0])
    # mySkid = 4947529

    mySkid = str(mySkid)

    response = requests.get(
        'https://neuropil.janelia.org/tracing/fafb/v14/{}/skeletons/{}/compact-detail'.format(project_id, mySkid),
        auth=auth  # ,
        # data = {'skeleton_id' : mySkid}
    )

    skelInfo = json.loads(response.content)
    skelInfo = skelInfo[0]
    myCoordinates = {}
    # myCoordinates = []
    for i in skelInfo:
        # myNode = [i[3], i[4], i[5]]
        myCoordinates[i[1]] = [i[3], i[4], i[5]]

    # return newList
    return myCoordinates


# currently returning just TNID, but can change to include all node info
def getTnid(tag, skeletonID=None):
    tag = str(tag)
    if skeletonID is None:
        skeletonID = 4947529  # defaults to DNright
    response = requests.get(
        'https://neuropil.janelia.org/tracing/fafb/v14/1/skeletons/{}/node-overview'.format(skeletonID),
    )
    myDict = json.loads(response.content)
    TNIDAndCoordinates = []
    a = None
    for i in myDict[2]:
        if tag == i[1]:
            a = i[0]
    for item in myDict[0]:
        if a is None:
            print('a is none')
        elif a == item[0]:
            TNIDAndCoordinates.append(item)
    return TNIDAndCoordinates[0]


##next step of below --> use filtered nodelist to get all connectors then get connector lookup table and find presynaptic partners by connector id

# input the TNID that you want as your starting point, output is a list with two sub-lists, the first of which contains lists of tree nodes that are downstream of the input and that treenodes relevant info, and the second containing connector id and connector info: 1) [id, parent_id, user_id, location_x, location_y, location_z, radius, confidence]. and 2) [treenode_id, connector_id, 0|1|2|-1, location_x, location_y, location_z]
# Bug - Can't get this request to return connectors
# notTNID should be a list of TNID based upon tags that indicate nodes downstream are not wanted
def getAllNodesDownStream(TNID, notTNID=None, mySkid=None):
    if mySkid is None:
        mySkid = 4947529
        mySkid = str(mySkid)
    else:
        mySkid = str(mySkid)

    response = requests.get(
        'https://neuropil.janelia.org/tracing/fafb/v14/{}/skeletons/{}/compact-detail'.format(project_id, mySkid),
        auth=auth,
        data={'with_connectors': True}
    )

    skelInfo = json.loads(response.content)
    allNodes = skelInfo[0]
    myPID = TNID[0]

    x = []
    myList = []
    myList.append(TNID)
    for i in allNodes:
        if i[1] == myPID:
            x.append(i)
            myList.append(i)
    foundNode = True
    '''
    while (foundNode is True):
        for i in allNodes:
            if i[1] in myList:
                myList.append(i[0])
                allNodes.remove(i)
                foundNode = True
                break
            else:
                foundNode = False'''
    '''x = []            
    for i in allNodes:
        if i[1] == myPID:
            x.append(i)'''
    allNodes = sorted(allNodes, key=lambda TNID: TNID[0])
    candidates = x
    # print(candidates)
    while not len(candidates) == 0:
        PNode = candidates.pop()
        if notTNID is None:
            children = list(filter(lambda node: node[1] == PNode[0], allNodes))
            # print('length = ', len(children), ', my children =', children, '\n')
        else:
            node = []
            children = []
            for i in allNodes:
                if i[1] == PNode[0]:  # and i[0] not in notTNID:
                    # children.append(i)
                    if i[0] not in notTNID:
                        children.append(i)
            # children = list(filter(lambda node: node[1] == PNode[0] and node[1] not in notTNID, allNodes ))
            # print('conditional not met: length = ', len(children), ', my children =', children, '\n')
        myList = myList + children
        candidates = candidates + children
    return myList


# helper function that combines the above two functions and returns downstream nodes of tag - use this function with either: 'start of anterior branch' or 'start of medial branch'
def getDownStreamNodes(skeletonID, tag, myCurNodes=None):
    if skeletonID is None:
        skeletonID = 4947529
    TNID = getTnid(tag, skeletonID)
    if myCurNodes is None:
        a = getAllNodesDownStream(TNID, mySkid=skeletonID)
    else:
        a = myCurNodes

    downStreamNodes = []
    for i in a:
        downStreamNodes.append(i[0])

    return downStreamNodes


# returns list of all connector nodes
def getAllConnectorInfo(skeletonID=None, polarity=None):
    if skeletonID is None:
        mySkid = 4947529
    else:
        mySkid = skeletonID
    if polarity is None:
        relation_type = 'postsynaptic'
    else:
        relation_type = polarity

    # gets connector ID for all nodes in given skeleton (output: {links:[[skleton ID, Connector ID, X, Y, Z, Confidence, User ID, TNID, Date Created, Date Modified]], tags:[...]
    response = requests.get(
        'https://neuropil.janelia.org/tracing/fafb/v14/{}/connectors/links/?skeleton_ids[0]={}&relation_type={}_to&with_tags=true'.format(
            project_id, mySkid, relation_type)  # ,
        # auth = auth,
        # data = {'skeleton_ids' : mySkid, 'relation_type' : 'postsynaptic_to'}
    )
    connectorInfo = json.loads(response.content)
    # print(connectorInfo)
    return connectorInfo


# returns a filtered list of all connector nodes(postsynaptic) within the range of downstream tag - should be used only with DN
def getConnectorInfo(tag, skeletonID=None, myCurNodes=None, polarity=None, connectorInfo=None):
    if skeletonID is None:
        skeletonID = 4947529
    if connectorInfo is None:
        connectorInfo = getAllConnectorInfo(skeletonID, polarity)
    else:
        connectorInfo = connectorInfo
    if myCurNodes is None:
        downStreamNodes = getDownStreamNodes(skeletonID, tag)
    else:
        downStreamNodes = myCurNodes

    myConnectorIDs = []
    for item in connectorInfo['links']:
        if item[7] in downStreamNodes:
            myConnectorIDs.append(item[1])

    return myConnectorIDs


# returns all connector ids for a given skeleton (for use with DN input neurons)
def getAllConnectors(skeletonID, polarity=None):
    if polarity is None:
        polarity = 'presynaptic'
    else:
        polarity = polarity
    connectorInfo = getAllConnectorInfo(skeletonID, polarity)

    myConnectors = {}
    myConnectorIDs = []
    # myConnectorCoordinates = []
    for item in connectorInfo['links']:
        # myConnectorIDs.append(item[1:5])
        myConnectors[item[1]] = item[2:5]
    # myConnectors['connectorID'] = myConnectorIDs

    return myConnectors


def getConnectorsByBranch(branch, skeletonID=None, connectorInfo=None):
    branch = str(branch)
    # if branch == 'anterior' or branch == 'medial':
    if branch == 'medial':
        myConnectors = getConnectorInfo(tag='start of {} branch'.format(branch), connectorInfo=connectorInfo)
    elif branch == 'anterior':
        myConnectors = getConnectorInfo(tag='end of lateral branch', connectorInfo=connectorInfo)
        myConnectors2 = getConnectorInfo(tag='start of anterior branch', connectorInfo=connectorInfo)
        myConnectors += myConnectors2
    elif branch == 'lateral':
        notTNID = []
        n1 = getTnid('start of descending tract')
        n2 = getTnid('end of lateral branch')
        n3 = getTnid('start of medial branch')
        n4 = getTnid('start of anterior branch')

        notTNID.append(n1[0])
        notTNID.append(n2[0])
        notTNID.append(n3[0])
        notTNID.append(n4[0])
        myTNID = getTnid('start of lateral branch')
        theseNodes = getAllNodesDownStream(myTNID, notTNID)
        myCurNodes = getDownStreamNodes(skeletonID, tag='start of lateral branch', myCurNodes=theseNodes)
        myConnectors = getConnectorInfo('start of {} branch'.format(branch), skeletonID=None, myCurNodes=myCurNodes)

        # myNodes1 = getDownStreamNodes(skeletonID, 'start of {} branch'.format(branch))
        # myNodes2 = getDownStreamNodes(skeletonID, 'start of {} branch'.format(branch))


    else:
        notTNID = []
        n4 = getTnid('end of soma tract')
        notTNID.append(n4[0])
        myTNID = getTnid('soma')
        theseNodes = getAllNodesDownStream(myTNID, notTNID)
        myCurNodes = getDownStreamNodes(skeletonID, tag='soma', myCurNodes=theseNodes)
        myConnectors = getConnectorInfo('soma', skeletonID=None, myCurNodes=myCurNodes)

    return myConnectors


def getNumSynByBranch(branch, skeletonID=None):
    myConnectors = getConnectorsByBranch(branch, skeletonID)
    numSynThisBranch = len(myConnectors)
    return numSynThisBranch


def getPresynapticPartners(skeletonID, tag):
    myPartners = []
    myConnectors = getConnectorInfo(skeletonID, tag)

    for i in myConnectors:
        connectorID = i
        response = requests.get(
            'https://neuropil.janelia.org/tracing/fafb/v14/{}/connectors/{}/'.format(project_id, connectorID)
        )
        thisPartner = json.loads(response.content)
        myPartners.append(thisPartner)
    return myPartners


'''def LPLC2_LPFilter(skid):
    #dorsal
    if yVal <= 220755:
        pass
    #ventral
    elif yVal >= 256000:
        pass
    #equatorial
    else:
        pass
    pass

## North      x: 348488 y: 220755 z: 256000
## Equatorial x: 351023 y: 236049 z: 251520
## South      x: 368987 y: 260891 z: 249440

#y = 177502.1 + (239885.3 - 177502.1)/(1 + (z/333652.4)^11.6237)'''

