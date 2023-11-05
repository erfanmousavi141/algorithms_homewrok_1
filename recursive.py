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

def f(sequence: list, seqLen: int):# -> None
    if seqLen == 1:
        thisElement = sequence[0]
        thisElementParent = thisElement[2]
        thisElementId = thisElement[0]
        index2parent_list.append((thisElementId, thisElementParent))
        return


    f([sequence[seqLen-1]], 1)
    f(sequence[0:seqLen-1], seqLen-1)


f(Data, len(Data))

parent2indexesDict = dict()

for index2parent in index2parent_list:
    try:
        parent2indexesDict[index2parent[1]].append(index2parent[0])
    except:
        parent2indexesDict[index2parent[1]] = []
        parent2indexesDict[index2parent[1]].append(index2parent[0])

print(parent2indexesDict)
