# Complete!

N = int(input())
shift = int(input())
arr = [N]

for i in range(shift):
    add = N*(10**(i+1))
    arr.append(add)

print(sum(arr))