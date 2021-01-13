def convertToReversedString(num):
    s = str(num)
    if num > 0:
        return s[::-1]
    else:
        s = s.strip("-")
        return "-" + s[::-1]
def compareToLimit(s, isNegative):
    limit1 = '214748364'
    if isNegative:
        limit2 = '8'
    else:
        limit2 = '7'
    sNum1 = s[:-1]
    sNum2 = s[-1]
    if int(sNum1) > int(limit1):
        return 0
    elif int(sNum1) < int(limit1):
        return 1
    else:
        if int(sNum2) > int(limit2):
            return 0
        else:
            return 1
def checkIfSignedInt(s):
    returnCase = 1
    isNegative = False;
    if "-" in s:
        isNegative = True
        s = s.strip("-")
    sLen = len(s)
    if sLen > 10:
        returnCase = 0
    elif sLen < 10:
        returnCase = 1
    else:
        returnCase = compareToLimit(s, isNegative)
    if returnCase == 0:
        return 0
    else:
        if isNegative:
            s = '-' + s
        return int(s)
            
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        else:
            s = convertToReversedString(x)
            return checkIfSignedInt(s)
