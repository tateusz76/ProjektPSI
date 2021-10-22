def rozdziel(aList,bList):
    parzysteA = []
    nieparzysteB = []
    for i in range(0, len(aList)):
        if i%2 == 0:
            parzysteA.append(aList[i])

    for i in range(0, len(bList)):
        if i%2 != 0:
            nieparzysteB.append(bList[i])

    return parzysteA + nieparzysteB


aList = [1,6,3,7,2,6,1,7]
bList = [7,4,2,7,1,5,3,4]

print(rozdziel(aList,bList))