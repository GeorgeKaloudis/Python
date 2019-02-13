alph=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
stats=[0]*26
file=raw_input("Give me a text file: ")
f=open(file,"r")
for line in f:
    for letter in line:
        if letter in alph: #value error: '\n' is not in list
            stats[alph.index(letter)]+=1
f.close()
for i in range (0,25):
    for j in range (25,i,-1):
        if stats[j]>stats[j-1]:
            t1=stats[j]
            stats[j]=stats[j-1]
            stats[j-1]=t1
            t2=alph[j]
            alph[j]=alph[j-1]
            alph[j-1]=t2

max=alph[0]
for i in range(25,0,-1):
    if stats[i]>0:
        min=alph[i]
        break
print max,min
f=open(file,"r+")
data=f.read()
data=data.replace(max,min.upper())
data=data.replace(min,max.upper())
f.close()
f=open(file,"w")
f.write(data)
f.close()
