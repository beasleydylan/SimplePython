def find_prime_factor(num):
    value = False
    for i in range(3,num,2):
        if num%i==0:
            for y in range(2,i):
                if i%y==0:
                    value = True
                    break
            if not value:
                yield i
what_num = int(input('What integer do you want prime factors of? '))
for i in list(find_prime_factor(what_num)):
    print(i)