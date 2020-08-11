point_one= input().split()
point_two= input().split()
t = int(input())

a = int(point_one[0])
b = int(point_one[1])
c = int(point_two[0])
d = int(point_two[1])

def find_distance(a, b, c, d):
	min_distance = (c-a) + (d-b)
	return min_distance

def check(a, b, c, d, t):
	min_distance = find_distance(a, b, c, d)
	if min_distance % 2 == 0 and t % 2 == 0:
		return 'Y'
	elif min_distance % 2 != 0 and t % 2 != 0:
		return 'Y'
	else:
		return 'N'

print(check(a, b, c, d, t))

