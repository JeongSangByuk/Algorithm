

import time

a = "123123"
b = list(a)

start =time.time()
print(a[2])

print((time.time() - start) * 100000)

start = time.time()

print(b[2])
print((time.time() - start) * 100000)


#print(b)
