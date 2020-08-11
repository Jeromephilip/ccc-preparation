r = 3
c = 4

grid = [[3, 10, 8, 4],    #  3  10  8   4
		 [1, 11, 12, 12], #  1  11  12  12
		 [6, 2, 3, 9]]    #  6  2   3   9

def find_divisors(num):
	out = []
	for i in range(1, num+1):
		if num % i == 0:
			out.append((int(i)-1, int(num/i)-1))
	return out

# Base Case --> If position == (r, c), return True. If len(positions) == 0, return False. 

def escape(position, r, c):
	num = grid[position[0]][position[1]]
	positions = find_divisors(num)
	for pos in positions:
		if pos[0] > r:
			positions.remove(pos)
		elif pos[1] > c:
			positions.remove(pos)
	print(positions)
	for p in positions:
		if p == (r, c):
			return 'yes'
			break
		else:
			escape(p, r, c)


print(escape((0, 0), 3, 4))
# escape((0, 0), 3, 4)
