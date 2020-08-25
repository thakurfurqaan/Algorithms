import time

start = time.time()

import math as m

class Solution:
    def climbStairs(self, n: int) -> int:
        ways = 0
        if n == 1:
            return(1)
        elif n == 2:
            return(2)
        elif n%2 == 0:
            ways = 2
            for i in range((n//2)+1,n):
                ways += int(m.factorial(i)/(m.factorial(n-i)*m.factorial(2*i-n)))
        else:
            ways = 1
            for i in range((n//2)+1,n):
                ways += int(m.factorial(i)/(m.factorial(n-i)*m.factorial(2*i-n)))
        return(ways)

# class Solution(object):
#     def climbStairs(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         memo = {}
        
#         def count(n):
#             if n == 1:
#                 return 1
#             elif n == 2:
#                 return 2
#             else:
#                 if n in memo.keys():
#                     return memo[n]
#                 else:
#                     memo[n] = count(n-1) + count(n-2)
#                     return memo[n]
        
#         return count(n)
            
a = Solution()
print(a.climbStairs(1000))

print(str(time.time() - start))

