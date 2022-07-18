import requests
import ascii

rootNodeId = "089ef556-dfff-4ff2-9733-654645be56fe"

def getNodes(nodeId):
    '''
    Get Nodes
    Get Nodes from a Given Node ID
    @param [nodeId]: Node IDs
    @return: Nodes
    '''
    flattenedNodeList = ",".join(nodeId)
    request = requests.get(f"https://nodes-on-nodes-challenge.herokuapp.com/nodes/{flattenedNodeList}")
    return request.json()
    

def traverseTree(root, nodeState = {}):
    '''
    Traverse Tree
    @param [root]: Root Node
    @param [nodeState]: Node State
    @return: Child Ids, Node State
    '''
    res = []
    if root:
        getNode = getNodes([root])
        nodeState[root] = getNode[0]['child_node_ids']
        for node in getNode:
            res.append(node["id"])
            for child in node["child_node_ids"]:
                childRes, nodeState = traverseTree(child, nodeState)
                res = res + childRes
    return res, nodeState

def findMostCommonlySharedNode(nodeState):
    '''
    Find Most Commonly Shared Node
    @param [nodeState]: Node State
    @return: Most Commonly Shared Node ID - String
    '''
    occurrences = {}
    for node in nodeState.keys():
        for child in nodeState[node]:
            if child in occurrences:
                occurrences[child] += 1
            else:
                occurrences[child] = 1
    return max(occurrences, key=occurrences.get)

if __name__ == "__main__":
    print(ascii.ascii_art)
    # Set the Root Node ID
    childrenIds, nodeState = traverseTree(rootNodeId)
    # Get the Total Number of Unique Nodes
    uniqueNodes = len(nodeState.keys())
    print("Total Number of Unique Nodes:", uniqueNodes)
    mostCommonSharedNode = findMostCommonlySharedNode(nodeState)
    print("Most Commonly Shared Node:", mostCommonSharedNode)
    