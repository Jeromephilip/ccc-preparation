# CCC / S2 / By: Jerome J.
# Here, it is important to note that the corners of the matrix is where the lowest numbers are found.
import numpy

dimensions = int(input())
rows = []
for r in range(dimensions):
    rows.append([int(x) for x in input().split()])
x = len(rows) - 1


def min_val(arr):
    result = numpy.where(arr == numpy.amin(arr))
    coords = list(zip(result[0], result[1]))
    coord = ", ".join(map(str, coords))
    return coord


value = str(min_val(rows))


def reverse(index, arr):
    if index == '(0, 0)':
        for i in range(dimensions):
            for j in range(dimensions):
                print(arr[i][j], end=" ")
            print()
    elif index == '(0, ' + str(x) + ')':
        for i in range(dimensions - 1, -1, -1):
            for j in range(dimensions):
                print(arr[j][i], end=" ")
            print()
    elif index == '(' + str(x) + ', 0)':
        for i in range(dimensions):
            for j in range(dimensions - 1, -1, -1):
                print(arr[j][i], end=" ")
            print()
    elif index == '(' + str(x) + ', ' + str(x) + ')':
        for i in range(dimensions - 1, -1, -1):
            for j in range(dimensions - 1, -1, -1):
                print(arr[i][j], end=" ")
            print()


reverse(min_val(rows), rows)
