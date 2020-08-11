pop = int(input())
N = int(input())
R = int(input())

s = [N]

for i in range(1000):
   k = N*R
   N = k
   s.append(k)
   if sum(s) > pop:
       print(i+1)
       break


