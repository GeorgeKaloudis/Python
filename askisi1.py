def sumIntervals(list):
    sum=0
    num=[]
    for i in range (0,len(list)):
        nlist=[]
        v=list[i]
        for k in range(v[0],v[1]+1):
            nlist.append(k)
        for j in range (nlist[0],nlist[-1]+1):
            if j not in num:
             num.append(j)
            else:
                if (j!=num[-1]):
                    nlist.remove(j)
        sum=sum+(nlist[-1]-nlist[0])
    return sum

x = input("Give me the number of intervals: ")
list=[]
for i in range(0,x):
    interval=[]
    print("Give me an interval: ")
    a=input("First number: ")
    b=input("Last number: ")
    print [a,b]
    interval.append(a)
    interval.append(b)
    list.append(interval)
print "The sum is",sumIntervals(list)
