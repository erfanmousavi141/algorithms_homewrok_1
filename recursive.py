#!/usr/bin/python


Data = [[0, "abc", 1], 
        [1, "asd", 2], 
        [2, "123", 1], 
        [3, "78", 1], 
        [4, "13", 3], 
        [5, "b", 2],
        [6, "abc", 1], 
        [7, "asd", 2], 
        [8, "123", 1], 
        [9, "78", 1], 
        [10, "13", 3], 
        [11, "b", 2],
        [12, "abc", 1], 
        [13, "asd", 2], 
        [14, "123", 1], 
        [15, "78", 1], 
        [16, "13", 3], 
        [17, "b", 2],  
        [18, "abc", 1], 
        [19, "asd", 2], 
        [20, "123", 1], 
        [21, "78", 1], 
        [22, "13", 3], 
        [23, "b", 2]]


index2parent_list = []

# inputs of this recursive function are an 2-d array (list)
# and the length of this array (int)
# this function recursively traveses the array
# then add a pair of key/value consisting every 
# node's ID and PARENT to a pre-defiened list (index2parent_list)
def f(sequence: list, seqLen: int):# -> None
    if seqLen == 1:
        thisElement = sequence[0] # Because the sequence is a 2-dimensional array
        thisElementParent = thisElement[2] # the last node is the PARENT
        thisElementId = thisElement[0] # the first node is the ID
        index2parent_list.append((thisElementId, thisElementParent)) # appending the node in a key/value form, from the ID and PARENT 
        return
        

    f([sequence[seqLen-1]], 1)
    f(sequence[0:seqLen-1], seqLen-1)


f(Data, len(Data))

parent2indexesDict = dict() # defining a dictionary
# the keys of this dict is the PARENTS and 
# the values of each key is a list, consisting the ID of the nodes that have the same PARENT

for index2parent in index2parent_list:
    # if the key is available in our dict, then just add the node's ID to the values list of this key 
    try:
        parent2indexesDict[index2parent[1]].append(index2parent[0])
    # if it is not, first, create that key with an empty list, 
    # then add the node's ID to the values list of the newly created key
    except:
        parent2indexesDict[index2parent[1]] = []
        parent2indexesDict[index2parent[1]].append(index2parent[0])

print(parent2indexesDict)
