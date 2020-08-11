N = int(input())

swifts = [int(i) for i in input().split()]
semaphores = [int(j) for j in input().split()]

# Loop through swifts and semaphores
	# Have two variables keep track of sums
	# Check if they are the same

swift_sum = 0
sema_sum = 0
out = 0


for i in range(N):
	swift_sum += swifts[i]
	sema_sum += semaphores[i]
	if swift_sum == sema_sum:
		out = i+1

print(out)
