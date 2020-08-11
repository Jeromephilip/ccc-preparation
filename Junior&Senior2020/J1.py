# Complete!

N = [int(input()) for i in range(3)]

s = 1
m = 2
l = 3

out = (N[0] * s) + (N[1]*m) + (N[2]*l)

if out >= 10:
    print('happy')
if out < 10:
    print('sad')



