class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        results = []
        stack = []

        for i in range(len(prices)-1,-1,-1):

            if len(stack) == 0:
                results.append(prices[i])
            elif (len(stack) > 0) and (stack[-1] <= prices[i]):
                results.append(prices[i] - stack[-1])
            elif (len(stack) > 0) and (stack[-1] > prices[i]): 
                while stack and (stack[-1] > prices[i]):
                    stack.pop()
                if not stack:
                    results.append(prices[i])
                else:
                    results.append(prices[i] - stack[-1])
            stack.append(prices[i])
        return results[::-1]
        