inp = input()

happy = 0
sad = 0



for i in range(len(inp)):
    if inp[i:i+3] == ":-)": # The input line here directly correlates to i.
        happy += 1
    elif inp[i:i+3] == ":-(":
        sad += 1


if happy > sad:
    print('happy')
if happy > 0 and sad > 0 and happy == sad:
    print('unsure')
if sad > happy:
    print('sad')
if happy == 0 and sad == 0:
    print('none')