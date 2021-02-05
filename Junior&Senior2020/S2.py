#exceeds time limit. change

r = int(input())
c = int(input())
grid = []
for i in range(r):
	grid.append([int(x) for x in input().split()])


found = []
found.append([r, c])


def can_escape(x):
	q = []
	for i in range(r):
		for j in range(c):
			if grid[i][j] == x:
				q.append([i, j])
	for pos in q:
		# base case
		if pos[0] == 0 and pos[1]==0:
			return True
		else:
			if [pos[0], pos[1]] not in found:
				found.append([pos[0], pos[1]])	
				if can_escape((pos[0]+1)*(pos[1]+1)):
					return True
	return False


if can_escape(r*c):
	print("yes")
else:
	print("no")