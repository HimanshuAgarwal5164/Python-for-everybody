fhand=open('xyz.txt','r')
s=fhand.read()
print("Text:\n",s)
print("Number of characters=",len(s))
print("Number of words=",len(s.split()))
