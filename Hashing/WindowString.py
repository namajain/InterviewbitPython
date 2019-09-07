ERROR = False
comb = {}


def calculatePossibleCombinations(inputStr):
    # Write your code here

    global ERROR
    global comb
    if ERROR:
        return 0
    if inputStr in comb:
        return comb[inputStr]
    if len(inputStr) == 0:
        return 1
    n = int(inputStr[-1])

    oneFlag = True if len(inputStr) > 1 and inputStr[-2] == '1' else False
    twoFlag = True if len(inputStr) > 1 and inputStr[-2] == '2' else False
    if n == 0:
        if not (oneFlag or twoFlag):
            ERROR = True
            return 0
        x = calculatePossibleCombinations(inputStr[:-2])
    elif oneFlag:
        x = calculatePossibleCombinations(inputStr[:-1]) + calculatePossibleCombinations(inputStr[:-2])
    elif twoFlag and n < 7:
        x = calculatePossibleCombinations(inputStr[:-1]) + calculatePossibleCombinations(inputStr[:-2])
    else:
        if len(inputStr) > 1:
            x = calculatePossibleCombinations(inputStr[:-1])
        else:
            x = 1
    if ERROR:
        return 0
    comb[inputStr] = x
    return x

print(calculatePossibleCombinations(''))