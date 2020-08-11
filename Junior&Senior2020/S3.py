permutation = str(input())
string = str(input())

# First we find all permutations of the string 'aab'
# We do this by placing all the permutations in an array

# Then we compare the permutations in the string using loops and the in operator.

def switch(string):
    c = []
    n = string
    for i in range(len(string)):
        c.append(n[-1:] + n[:-1])
        n = n[-1:] + n[:-1]
    return c

count = 0
for i in switch(permutation):
	if i in string:
		count += 1

print(count)



