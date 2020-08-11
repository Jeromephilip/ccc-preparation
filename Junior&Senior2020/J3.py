cases = int(input())
arr = [str(input()) for k in range(cases)]

x = [list(map(int, sub.split(','))) for sub in arr]

xcoords = []
ycoords = []

for k in x:
    xcoords.append(k[0])
    ycoords.append(k[1])

blx = float('inf')
bly = float('inf')
trx = 0
tryy = 0

for i in xcoords:
    if i < blx:
        blx = i
    if i > trx:
        trx = i

for j in ycoords:
    if j < bly:
        bly = j
    if j > tryy:
        tryy = j


print(str(blx-1) + ', ' + str(bly-1))
print(str(trx+1) + ', ' + str(tryy+1))

# https://www.geeksforgeeks.org/python-convert-list-of-strings-to-list-of-tuples/ -- Geeks for Geeks, string to tuple.
