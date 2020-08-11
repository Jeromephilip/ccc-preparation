# S1 - Snow Calls
# Finished

cases = int(input())
test = [str(input()) for n in range(cases)]

new = []

values = {'A':'2', 'B':'2', 'C':'2', 'D':'3', 'E':'3', 'F':'3', 
'G':'4', 'H':'4', 'I':'4', 'J':'5', 'K':'5', 'L':'5', 'M':'6', 'N':'6', 
'O':'6', 'P':'7', 'Q':'7', 'R':'7',
'S':'7', 'T':'8', 'U':'8', 'V':'8', 'W':'9', 'X':'9', 'Y':'9', 'Z':'9'} 

for i in test:
	new.append(i.replace('-',''))

out_arr = []
for j in new:
	for k in j:
		if k in values.keys():
			j = j.replace(k, values[k])
	out_arr.append(j)

second_last = []
for string in out_arr:
	string = '{}-{}-{}'.format(string[:3], string[3:6], string[6:10])
	second_last.append(string)

for final in second_last:
	print(final)