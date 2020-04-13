import sys
input = sys.stdin.readline

N = int(input())
prices = [list(map(int, input().split())) for _ in range(N)]
costs = [[0] * 3 for _ in range(N)]

for i in range(N):
    if i == 0:
        costs[i][0] = prices[i][0]
        costs[i][1] = prices[i][1]
        costs[i][2] = prices[i][2]
        continue
    
    for j in range(3):
        candidatePrice = 1000001

        for k in range(3):
            if not j == k:
                if candidatePrice > costs[i - 1][k]:
                    candidatePrice = costs[i - 1][k]
            
        costs[i][j] = prices[i][j] + candidatePrice
    
print(min(costs[-1]))