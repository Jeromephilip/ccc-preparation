# S1 
# Jerome Jeby Philip 
cases = int(input())
inp = []
times = []
positions = []

# Sorting into seperate arrays
for i in range(cases):
    t, d = map(int, input().split())
    inp.append([t, d])	    	

# Sorts array according to time
inp.sort(key = lambda x: x[0])

for j in inp:
	times.append(j[0])
	positions.append(j[1])

# Finding the position difference
def find_tree_position(pos):
	position_diff = []
	for i in range(len(pos)-1):
		diff = abs(pos[i] - pos[i+1]) # [100, 120, 50]
		position_diff.append(diff)
	return position_diff

# Finding the time difference
def find_tree_times(time):
	times_diff = []
	for i in range(len(time)-1):
		diff = abs(time[i] - time[i+1])
		times_diff.append(diff)
	return times_diff

final_arr = []
new_positions = find_tree_position(positions) # [20, 70]
new_times = find_tree_times(times) # [10, 10]

# Finding the speed (s = d / t)
for i in range(len(positions)-1):
	final_num = new_positions[i] / new_times[i]
	final_arr.append(final_num)

# Print out the max of array
print(max(final_arr))