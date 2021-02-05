# S2 - Mouse Move
# Not Finished


start = [0, 0] # Needed
moves = [] # Needed
check = [1, 1] # Only needed for inputs

while check != [0, 0]:
	t, d = map(int, input().split())
	moves.append([t, d])
	check[0] = t
	check[1] = d

# Needed
dimensions = moves[0]
moves.remove(moves[0])
moves.pop()

def update(start, move, dimensions):
	updated = [0, 0]
	updated[0] = start[0] + move[0]
	if updated[0] > dimensions[0]:
		updated[0] = dimensions[0] 
	elif updated[0] < 0:
		updated[0] = 0
	updated[1] = start[1] + move[1]
	if updated[1] > dimensions[1]:
		updated[1] = dimensions[1] 
	elif updated[1] < 0:
		updated[1] = 0
	return updated

for move in moves:
	print(str(update(start, move, dimensions)[0]) + ' ' + str(update(start, move, dimensions)[1]))
	start = update(start, move, dimensions)
