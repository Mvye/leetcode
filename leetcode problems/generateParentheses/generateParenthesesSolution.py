def split(openP, closedP, currentString):
    if (openP == 0):
        return [currentString + ')'*closedP]
    if (openP == closedP):
        return split(openP-1, closedP, currentString+'(')
    elif (openP < closedP):
        return split(openP-1, closedP, currentString+'(') + split(openP, closedP-1, currentString+')')
    else:
        return "this wont happen"
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return split(n, n, "")
