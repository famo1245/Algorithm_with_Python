import sys

input = sys.stdin.readline
n, m = map(int, input().split())

A = list(map(int, input().split()))
S = [0] * n
R = [0] * m
S[0] = A[0]
answer = 0

for i in range(1, n):
    S[i] = S[i-1] + A[i]

for i in range(n):
    reminder = S[i] % m
    if reminder == 0:
        answer += 1
    R[reminder] += 1

for i in range(m):
    if R[i] > 1:
        answer += (R[i] * (R[i] - 1) // 2)

print(answer)
