# Cycle Shifts

test = str(input())
cycle = str(input())
length_c = len(cycle)
length_t = len(test)


def switch(cycle):
    c = []
    n = cycle
    for i in range(len(cycle)):
        c.append(n[-1:] + n[:-1])
        n = n[-1:] + n[:-1]
    return c


cycle_arr = switch(cycle)

yes = 0

for i in range(length_t):
    for j in cycle_arr:
        if test[i:i + length_c] == j:
            yes += 1

if yes == 0:
    print('no')
else:
    print('yes')
