N = int(input())
tides = sorted([int(x) for x in input().split()]) # 2 3 7 10 40 50 90 110
low_tides = []
high_tides = []
out = []

for i in range(int(N/2)):
	low_tides.append(tides[i])

for j in reversed(range(int(N/2), N)):
	high_tides.append(tides[j])

l_tides = low_tides[::-1]
h_tides = high_tides[::-1] 


for k in range(int(N/2)):
	out.append(l_tides[k])
	out.append(h_tides[k])

for num in out:
	print(num, end=" ")