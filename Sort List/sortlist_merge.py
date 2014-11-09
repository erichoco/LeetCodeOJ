#/usr/local/env python

# Problem link: https://oj.leetcode.com/problems/sort-list/

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

        last = self.getLastOfList1(head)
        head2 = last
        head2 = self.pointNextNode(head2)
        last.next = None

        head = self.sortList(head)
        head2 = self.sortList(head2)

        return self.mergeList(head, head2)

    def getLastOfList1(self, head):
        last = head
        pointer = head
        isEven = False
        while not pointer.next is None:
            pointer = self.pointNextNode(pointer)
            if isEven:
                last = self.pointNextNode(last)
            isEven = not isEven
        return last

    def mergeList(self, head1, head2):
        head, pointer = None, None
        pointer1 = head1
        pointer2 = head2
        while not pointer1 is None and not pointer2 is None:
            tmpPointer = None
            if pointer1.val <= pointer2.val:
                tmpPointer = pointer1
                pointer1 = self.pointNextNode(pointer1)
            else:
                tmpPointer = pointer2
                pointer2 = self.pointNextNode(pointer2)
            if head is None:
                head = tmpPointer
                pointer = tmpPointer
            else:
                pointer.next = tmpPointer
                pointer = self.pointNextNode(pointer)
        if pointer1 is None:
            pointer.next = pointer2
        elif pointer2 is None:
            pointer.next = pointer1
        return head

    def pointNextNode(self, node):
        tmp = node.next
        node = None
        node = tmp
        return node

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
