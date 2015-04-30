class Solution:
    # @param {integer} k
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, k, prices):
        if 2 > len(prices):
            return 0
        diffLi = [0]
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            if 0 < diff:
                if 0 <= diffLi[-1]:
                    diffLi[-1] += diff
                else:
                    diffLi.append(diff)
            elif 0 > diff:
                if 0 >= diffLi[-1]:
                    diffLi[-1] += diff
                else:
                    diffLi.append(diff)
        if 1 == len(diffLi) and 0 >= diffLi[0]:
            return 0
        else:
            if 0 > diffLi[0]:
                diffLi.pop(0)
            if 0 > diffLi[-1]:
                diffLi.pop()
        transactionExceed = len([d for d in diffLi if d > 0]) - k
        for i in range(transactionExceed):
            gain = [d for d in diffLi if d >= 0]
            loss = [-d for d in diffLi if d < 0]
            if 0 < len(gain) and 0 < len(loss):
                if min(gain) < min(loss):
                    idx = diffLi.index(min(gain))
                else:
                    idx = diffLi.index(-min(loss))
            elif 0 == len(loss):
                idx = diffLi.index(min(gain))
            elif 0 == len(gain):
                return 0
            if 0 == idx:
                diffLi = diffLi[2:]
            elif len(diffLi)-1 == idx:
                diffLi = diffLi[:-2]
            else:
                diffLi[idx-1:idx+2] = [sum(diffLi[idx-1:idx+2])]
        return sum([d for d in diffLi if d > 0])

