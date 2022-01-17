from itertools import permutations

tmp = []
for i in permutations(['1','2','3','4'], 4):
    tmp.append(''.join(i))

print(tmp)