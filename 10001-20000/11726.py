n = int(input())

cnt = [1,2]

for i in range(n):
    cnt.append(cnt[i]+cnt[i+1])

print(cnt[n-1]%10007)