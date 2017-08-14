from collections import Counter
def checkIllumination(N, lamps, queries):
    # init
    result = []
    lamps = tuplerize(lamps)
    queries = tuplerize(queries)

    lightSiteTable = Counter()
    for i in range(len(lamps)):
        lightSiteTable[lamps[i][0] * N + lamps[i][1]] += 1
        lightSiteTable[(lamps[i][0], lamps[i][1])] += 1
    lightTable = Counter()

    for i in range(len(lamps)):
        lightSite = lamps[i]
        processLightSite(N, lightSite, lightTable, True)
    for i in range(len(queries)):
        # print "unclosed", sorted(lightTable.items())
        diffi = [-1, 0, 1]
        diffj = [-1, 0, 1]
        workSite = queries[i]
        workSiteRow, workSiteCol = workSite[0], workSite[1]
        for diffI in diffi:
            for diffJ in diffj:
                potentialSite = (workSiteRow + diffI, workSiteCol + diffJ)
                if potentialSite in lightSiteTable:
                    processLightSite(N, potentialSite, lightTable, False)
        # print "closed", sorted(lightTable.items())
        if lightTable[workSite[0] * N + workSite[1]] == 0:
            result.append("DARK")
        else:
            result.append("LIGHT")
        for diffI in diffi:
            for diffJ in diffj:
                potentialSite = (workSiteRow + diffI, workSiteCol + diffJ)
                if potentialSite in lightSiteTable:
                    processLightSite(N, potentialSite, lightTable, True)
    return result



# def isIlluminated(lightSite, gridSite):
#   if gridSite[0] == lightSite[0] or gridSite[1] == lightSite[1]:
#       return True
#   if gridSite[0] + gridSite[1] == lightSite[0] + lightSite[1]:
#       return True
#   if gridSite[0] - gridSite[1] == lightSite[0] - lightSite[1]:
#       return True
#   return False

def processLightSite(N, lightSite, lightTable, turnOn):
    # process row
    lightSiteRow, lightSiteCol = lightSite[0], lightSite[1]
    k = 1
    while k + lightSiteCol <= N:
        if turnOn:
            lightTable[lightSiteRow * N + k + lightSiteCol] += 1
        else:
            lightTable[lightSiteRow * N + k + lightSiteCol] -= 1
        k += 1
    k = 1
    while lightSiteCol - k > 0:
        if turnOn:
            lightTable[lightSiteRow * N +  lightSiteCol - k] += 1
        else:
            lightTable[lightSiteRow * N + lightSiteCol - k] -= 1
        k += 1

    # process col
    k = 1
    while lightSiteRow + k <= N:
        if turnOn:
            lightTable[(lightSiteRow + k) * N + lightSiteCol] += 1
        else:
            lightTable[(lightSiteRow + k) * N + lightSiteCol] -= 1
        k += 1
    k = 1
    while lightSiteRow - k > 0:
        if turnOn:
            lightTable[(lightSiteRow - k) * N + lightSiteCol] += 1
        else:
            lightTable[(lightSiteRow - k) * N + lightSiteCol] -= 1
        k += 1

    # process diag 1
    k = 1
    while lightSiteRow - k > 0 and lightSiteCol + k <= N:
        if turnOn:
            lightTable[(lightSiteRow - k) * N + lightSiteCol + k] += 1
        else:
            lightTable[(lightSiteRow - k) * N + lightSiteCol + k] -= 1
        k += 1
    k = 1
    while lightSiteRow + k <= N and lightSiteCol - k > 0:
        if turnOn:
            lightTable[(lightSiteRow + k) * N + lightSiteCol - k] += 1
        else:
            lightTable[(lightSiteRow + k) * N + lightSiteCol - k] -= 1
        k += 1

    # diag 2
    k = 1
    while lightSiteRow + k <= N and lightSiteCol + k <= N:
        if turnOn:
            lightTable[(lightSiteRow + k) * N + lightSiteCol + k] += 1
        else:
            lightTable[(lightSiteRow + k) * N + lightSiteCol + k] -= 1   
        k += 1
    k = 1
    while lightSiteRow - k > 0 and lightSiteCol - k > 0:
        if turnOn:
            lightTable[(lightSiteRow - k) * N + lightSiteCol - k] += 1
        else:
            lightTable[(lightSiteRow - k) * N + lightSiteCol - k] -= 1
        k += 1

    if turnOn:
        lightTable[lightSiteRow * N + lightSiteCol] += 1
    else:
        lightTable[lightSiteRow * N + lightSiteCol] -= 1

# lightList = [(1,1), (2,2)]
# workList = [(1,3),(2,3)]

lightList = [[4,3], [4,4]]
workList = [[3,4],[7,6]]
def tuplerize(arr):
    tupleList = []
    for item in arr:
        tupleList.append((item[0], item[1]))
    return tupleList

N = 8

print checkIllumination(N, lightList, workList)