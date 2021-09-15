dir = []
len = []
area = 0

N = int(input())
for i in range(6):
    a, b = input().split()
    dir.append(int(a))
    len.append(int(b))

if dir[0] != dir[4] and dir[1] != dir[3]:
    area = abs(len[3]*len[4] - len[0]*len[1])
else:
    area = len[3]*len[4] + len[0]*len[1]

print(N*area)