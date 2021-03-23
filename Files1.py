n=0
s=""
fhand=open('xyz.txt','r')
for line in fhand:
    print(line,end="")         #Print text of file without storing
    n=n+1                      #Number of lines
    s=s+line                   #Store text
print("\nNumber of lines=",n)
print("Number of characters=",len(s))
print("Number of words=",len(s.split()))
print(s)                       #Print text after storing
