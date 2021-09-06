
def selfnumber():
    gen = []
    for i in range(10000):
        num = 0
        for j in str(i):
            num += int(j)
        gen.append(i+num)

    result = []
    for item in range(10000):
        if not item in gen:
            result.append(item)

    for i in range(len(result)):
        print(result[i])

selfnumber()