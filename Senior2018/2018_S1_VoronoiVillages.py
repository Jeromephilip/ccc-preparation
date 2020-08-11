# CCC / S1 / By: Jerome J.

cases = int(input())
arr = sorted([int(input()) for i in range(cases)])
# 0, 4, 10, 15, 16


def chk_neighbor(arr):
    min_val = float("inf")
    for i in range(1, len(arr)-1):
        dist_left = (arr[i] - arr[i-1])/2
        dist_right = abs((arr[i+1] - arr[i])/2)
        total_dist = dist_left + dist_right
        if total_dist < min_val:
            min_val = total_dist
    return min_val


print(chk_neighbor(arr))
