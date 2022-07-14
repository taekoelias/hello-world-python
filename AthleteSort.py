# INPUT
# The first line contains N and M separated by a space.
# The next N lines each contain M elements.
# The last line contains K.
#
# OUTPUT
# Print the N lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.
#

nm = input().split()

n = int(nm[0])

m = int(nm[1])

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

k = int(input())

arr.sort(key=lambda x: x[k])

for i in arr:
    for j in i:
        print(j, end=' ')
    print()