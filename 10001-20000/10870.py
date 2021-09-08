n = int(input())

fibonacci = [0,1]

for i in range(n-1):
    fibonacci.append(fibonacci[i]+fibonacci[i+1])

print(fibonacci[n])