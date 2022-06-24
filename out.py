# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        tem = ListNode(-10000)
        tem.next = l1
        l1 = tem

        s1, p1, p2 = l1, l1, l2
        while(l2 != None):
            while(l1 != None and l1.val <= l2.val):
                p1,l1 = l1,l1.next
                #l1 =  l1.next

            l2, p1.next, p2.next = l2.next, p2, l1
            p1, p2 = p2, l2


        #删除第一个节点
        s1 = s1.next
        return s1