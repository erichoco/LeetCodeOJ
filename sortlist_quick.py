#/usr/local/env python

# Problem link: https://oj.leetcode.com/problems/sort-list/
# Note: This will receive TLE as it's worst case is O(n^2)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # may exceed max recursion call limit on long linked-list
    def printList(self):
        print self.val,
        if self.next:
            self.next.printList()
        else:
            print ""

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if head is None:
            return
        if head.next is None:
            return head

        pivotVal = head.val
        curNode = head

        # partition
        headLess, headGreat = None, None
        tailLess, tailGreat = None, None
        while not curNode.next is None:
            nextNode = curNode.next
            if nextNode.val <= pivotVal:
                if headLess is None:
                    headLess = nextNode
                if curNode is tailGreat:
                    tailGreat.next = None
                    if not tailLess is None:
                        tailLess.next = nextNode
                tailLess = None
                tailLess = nextNode
            else:
                if headGreat is None:
                    headGreat = nextNode
                if curNode is tailLess:
                    tailLess.next = None
                    if not tailGreat is None:
                        tailGreat.next = nextNode
                tailGreat = None
                tailGreat = nextNode
            curNode = None
            curNode = nextNode

        # recursive
        if not headLess is None:
            headLess = self.sortList(headLess)
        if not headGreat is None:
            headGreat = self.sortList(headGreat)

        # merge
        if not headLess is None:
            curNode = headLess
            while not curNode.next is None:
                curNode = curNode.next
            curNode.next = head
        else:
            headLess = head
        head.next = headGreat

        return headLess

def main():
    # put any list you want to sort
    li = [10, 3, 2, 4, 7, 4, 1, 11, 39, 2039, 230981, 8, 294, 443]

    a = ListNode(li[0])
    curNode = a
    for idx, val in enumerate(li):
        if 0 == idx:
            continue
        curNode.next = ListNode(val)
        tmp = curNode.next
        curNode = None
        curNode = tmp

    sol = Solution()
    sortA = sol.sortList(a)

    # sortA.printList()

if __name__ == '__main__':
    main()

