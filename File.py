f1 = open("file1.txt", "r")

f2 = open("file2.txt", "r")

f3 = open("file3.txt", "a+")
data1 = f1.readlines()
data2 = f2.readlines()
ldata1 = len(data1)
ldata2 = len(data2)
n = max(ldata1, ldata2)
f1.close()
f2.close()
f1 = open("file1.txt", 'r')
f2 = open("file2.txt", 'r')

for i in range(n):
    p1 = f1.readline()
    if (len(p1) != 0):
        f3.write(p1)
        p2 = f2.readline()
        if (len(p2) != 0):
            f3.write(p2)

f1.close()
f2.close()
f3.close()