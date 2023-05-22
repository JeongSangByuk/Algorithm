import math
import sys
from collections import deque, defaultdict
import itertools
from heapq import heappush, heappop

# 01 = a
# 02 = a a
# 03 = a a a
# 04 = a a a a
# 05 = a a a a a

# 06 = a  a  a ca cc cv  => 3 + 3
# 06 = a  a ca cc cv cv  => 2 + 2 + 2
# 06 = a ca cc cv cv cv  => 1 + 1 + 1 + 1

# 07 =  a  a  a t1 ca cc cv  => 4 * 2
# 07 =  a  a t2 ca cc cv cv  => 3 * 3
# 07 =  a t3 ca cc cv cv cv  => 2 * 4
# 07 = t4 ca cc cv cv cv cv  => t4값을 이용해서 t1 값이 결정이 됨. DP

# n>=6부터는, a a a 보다 무조건 복붙하는게 이득이다.
# 복붙되는 값의 최댓값을 dp에 저장하는 것.

n = int(input())

dp = [i for i in range(102)]

for i in range(6, 101):
    dp[i] = max(dp[i - 3] * 2, dp[i-4]*3, dp[i-5]*4)

print(dp[n])
