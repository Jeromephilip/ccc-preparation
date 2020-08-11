# Complete!


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def check_sums(num):
    max_num = num * 2
    for i in range(3, max_num):
        for j in range(3, max_num):
            if is_prime(i) and is_prime(j):
                sum = i + j
                if sum/2 == num:
                    return [i, j]


c = int(input())
arr = [int(input()) for x in range(c)]

for i in arr:
    s = check_sums(i)
    print(s[0], s[1])
    # print(str(s[0]) + '  ' + str(s[1]))



# lines = []
# while True:
#     line = int(input())
#     if line:
#         lines.append((line))
#     else:
#         break

# for i in lines:
#     output = str(check_sums(i)).strip('()')
#     print(output)
