d={10:'xyz',4:'abc',1:'zzz',7:'aaa'}
print("Sorting wrt keys:")
l=d.items()
l=sorted(l)
d=dict(l)
print(d)




d={10:'xyz',4:'abc',1:'zzz',7:'aaa'}
print("Sorting wrt values:")
l=d.items()
l1=[]
for (k,v) in l:
    l1.append((v,k))
l1=sorted(l1)
l=[]
for (v,k) in l1:
    l.append((k,v))
d=dict(l)
print(d)
