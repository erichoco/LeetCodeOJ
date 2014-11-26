#/usr/local/bin python

class Stack:
    def __init__(self):
        self.data = []

    def push(self, datum):
        self.data.append(datum)

    def pop(self):
        return self.data.pop()

    def peek(self):
        try:
            return self.data[-1]
        except:
            return None

class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        lenA = len(A)

        if 3 > lenA:
            return 0

        stack = Stack()
        water, curMax = 0, 0
        for i, v in enumerate(A):
            if i == lenA-1:
                break

            stack.push(v)
            if v > curMax:
                curMax = v

            nextV = A[i+1]
            if nextV > curMax:
                nextV = curMax

            if v < nextV:
                water += self.fillWater(stack, nextV)

        return water

    def fillWater(self, stack, curL):
        thisWater, prevWater = 0, 0
        if stack.peek() < curL:
            thisWater = curL - stack.pop()
            prevWater = self.fillWater(stack, curL)
            stack.push(curL)
        return thisWater + prevWater


def main():
    test = [0,1,0,2,1,0,1,3,2,1,2,1]

    solution = Solution()
    print solution.trap(test)

if __name__ == '__main__':
    main()