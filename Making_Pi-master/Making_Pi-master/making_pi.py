def make_pi():
    num = 4
    for i in range(1,500,2):
        yield (num/i)
        num*=-1
    
pi = list(make_pi())
smu = 0
for i in pi:
    smu += i
print(smu)