def number(n):
    a = [int(d) for d in str(n)]
    temp = 0
    for i in range(len(a)):
        # print(i)
        temp = a[i] + temp
    final = int(n) // temp
    return final

n = input('Enter Your Number :- ')
print(number(n))
