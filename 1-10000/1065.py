N = int(input())

H = list(range(1,100))

n = 100
while N >= n:
    list = []
    for i in str(n):
        list.append(int(i))
    if list[1]-list[0] == list[2] - list[1]:
        H.append(n)
    n += 1


H = [x for x in H if x<=N]
print(len(H))