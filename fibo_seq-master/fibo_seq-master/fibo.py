def fibo(num):
    a = 0
    b = 1
    sum1 = a+b
    while b <= num+1:
        yield a,b
        a,b = sum1,sum1+b
        sum1 = a+b
x = int(input('Enter a number for the fibonacci sequence to end at!'))
lis = [i for i in fibo(x)]
print(lis)