N = int(input())
A = [int(x) for x in input().split()]
B, C = map(int, input().split())
count = N

for i in range(N):
    if A[i]<B:
        continue
    count += (A[i]-B)//C
    if (A[i]-B)%C != 0:
        count += 1

print(count)