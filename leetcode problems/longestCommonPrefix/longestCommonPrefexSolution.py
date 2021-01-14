def compareStrings(smallString, bigString):
    newP = ""
    for i in range(len(smallString)):
        if smallString[i] == bigString[i]:
            newP = newP+smallString[i]
        else:
            break
    return newP
        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        currentP = strs[0]
        for s in strs:
            sL = len(s)
            pL = len(currentP)
            if sL == 0 or pL == 0:
                return ""
            elif sL >= pL:
                if currentP in s[:pL]:
                    continue
                else:
                    currentP = compareStrings(currentP, s)
            else:
                if s in currentP[:sL]:
                    currentP = s
                    continue
                else:
                    currentP = compareStrings(s, currentP)
        return currentP
