n = int(input())
m = int(input())
x = int(input())
count = 0
#a = list(range(1, n * m + 1, m))
a = []

for i in range(1, n * m + 1, m):
    a.append(i)
    if i < x:
        count+=1

print(a)

if count == 0:
    print("None")
else:
    print("count =",count)