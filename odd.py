import math;
list= list(map(int,input().split(',')))


oddNum = [i for i in list if (int(i) % 2 != 0)]
for i in  oddNum:
    print(i**2)




