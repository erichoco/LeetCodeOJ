#/usr/local/env python

# Problem link: https://oj.leetcode.com/problems/sort-colors/

class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        if len(A) <= 1:
            return
        pointer = [0, 0]
        for idx, val in enumerate(A):
            if val == 0:
                pointer[0] += 1
                pointer[1] += 1
                if 1 == A[pointer[0]-1]:
                    A[pointer[0]-1], A[idx] = A[idx], A[pointer[0]-1]
                if 2 == A[pointer[1]-1]:
                    A[pointer[1]-1], A[idx] = A[idx], A[pointer[1]-1]
            elif val == 1:
                pointer[1] += 1
                A[pointer[1]-1], A[idx] = A[idx], A[pointer[1]-1]
        print A
        return

def main():
    colors = [1,2,0,1,2,0,0]
    sol = Solution()
    sol.sortColors(colors)

if __name__ == '__main__':
    main()