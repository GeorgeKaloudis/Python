file=raw_input("Give me a python file name: ")
while file[-3:]!=".py":
    file=raw_input("Give me a python file name: ")
f=open(file,"r")
lines = f.readlines()
f.close()
f = open(file,"w")
for line in lines:
    c1=0
    c2=0
    if "#" not in line:
        f.write(line)
    else:
        p=line.index("#")
        for i in range(0,p):
            if line[i]=="'":
                c1+=1
            if line[i]=='"':
                c2+=1
        if (c1 % 2 !=0) or (c2 % 2 !=0):
            f.write(line)
        else:
            f.write(line[0:line.index("#")]+"\n")
f.close()
