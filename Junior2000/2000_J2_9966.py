# Complete!


m = int(input())
n = int(input())


def flip(a):
    arr = []
    for i in a:
        if i == '1':
            arr.append(i.replace('1', '1'))
        if i == '0':
            arr.append(i.replace('0', '0'))
        if i == '6':
            arr.append(i.replace('6', '9'))
        if i == '8':
            arr.append(i.replace('8', '8'))
        if i == '9':
            arr.append(i.replace('9', '6'))
        else:
            continue
    reverse = arr[::-1]  # Reversing an array
    x = str(''.join(reverse))  # Joining elements in an array
    return x


out_arr = []

for i in range(m, n):
    x = str(i)
    y = flip(str(i))
    if x == y:
        out_arr.append(i)

out = 0

for i in out_arr:
    out += 1

print(out)





# for i in range(10):
#     b = int(flip(str(i)))
#     if i == b:
#         return




