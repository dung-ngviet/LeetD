class Solution(object):
    def greatestCommonDivisor(self, a, b):
        if a == 0:
            return b
        else:
            return b % a

    def hasGroupsSizeX(self, deck):
        deckItemsCount = [0] * 10000
        for item in deck:
            deckItemsCount[item] += 1

        gcd = 0
        for actualItemCount in deckItemsCount:
            gcd = self.greatestCommonDivisor(gcd, actualItemCount)

        return gcd >= 2

print(Solution().hasGroupsSizeX([1,1,1,2,2,2,3,3]))
