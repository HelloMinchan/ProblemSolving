import sys
input = sys.stdin.readline

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            triangle[i][j] += triangle[i - 1][j]
        elif j == i:
            triangle[i][j] += triangle[i - 1][j - 1]
        else:
            if triangle[i - 1][j - 1] > triangle[i - 1][j]:
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                triangle[i][j] += triangle[i - 1][j]

print(max(triangle[n - 1]))