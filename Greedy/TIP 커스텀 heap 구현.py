import math
import sys
from collections import deque
from collections import defaultdict
import itertools
from heapq import heappush, heappop
from bisect import bisect_left


class Node:

    def __init__(self, time, y, x):
        self.time = time
        self.y = y
        self.x = x

    def get_list(self):
        return list((self.time, self.y, self.x))

    def __lt__(self, o):

        # 내림차순, 오름차순은 부등호 반대로
        if self.time < o.time:
            return True

        elif self.time == o.time:

            if self.y < o.y:
                return True

            elif self.y == o.y:
                return self.x < o.x

            return False

        return False

que = []
heappush(que, Node(3, 1, 1))
heappush(que, Node(3, 2, 1))
heappush(que, Node(2, 2, 3))
heappush(que, Node(2, 1, 3))
heappush(que, Node(3, 1, 3))
heappush(que, Node(1, 1, 1))
heappush(que, Node(1, 2, 3))
heappush(que, Node(3, 2, 2))

while que:
    print(heappop(que).get_list())

