# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def listToNumber(l: ListNode):
        num = ""
        cur = l
        while(True):
            s = str(cur.val)
            num = s + num
            if(cur.next is None):
                break
            cur = cur.next
        return num
def numberToList(num) -> ListNode:
    previous = ListNode(int(num[0]), None)
    for i in range(1,len(num)):
        curr = ListNode(int(num[i]), previous)
        previous = curr
    return previous
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = int(listToNumber(l1))
        num2 = int(listToNumber(l2))
        sumNum = str(num1+num2)
        sumList = numberToList(sumNum)
        return sumList
