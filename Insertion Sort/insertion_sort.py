#/usr/local/env python

# Problem link: https://oj.leetcode.com/problems/insertion-sort-list/

# To acheive O(1) space complexity for singly-linked list (not required),
# this version alters the original insertion sort,
# which searches for insertion position from the beginning.
# (and would failed on sorted testing data due to TLE)

import sys
sys.setrecursionlimit(10000)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def printList(self):
        print self.val,
        if self.next:
            self.next.printList()
        else:
            print ""

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head is None or head.next is None:
            return head
        nextNode = head.next
        sortHead = head
        sortHead.next = None
        while not nextNode is None:
            node = nextNode
            nextNode = node.next
            if node.val <= sortHead.val:
                node.next = sortHead
                sortHead = node
            else:
                sortNode = sortHead
                while True:
                    if sortNode.next is None:
                        sortNode.next = node
                        node.next = None
                        break
                    elif node.val <= sortNode.next.val:
                        node.next = sortNode.next
                        sortNode.next = node
                        break
                    sortNode = sortNode.next
        return sortHead

def listToListNode(li):
    if li is None:
        return None
    a = ListNode(li[0])
    curNode = a
    for idx, val in enumerate(li):
        if 0 == idx:
            continue
        curNode.next = ListNode(val)
        curNode = curNode.next
    return a

def main():
    # put any list you want to sort
    li = [10, 3, 2, 4, 7, 4, 1, 11, 39, 2039, 230981, 8, 294, 443]

    sol = Solution()
    sortA = sol.insertionSortList(listToListNode(li))

    sortA.printList()

if __name__ == '__main__':
    main()
