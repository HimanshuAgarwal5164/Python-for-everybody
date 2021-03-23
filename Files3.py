try:
    fname=input("Enter file name")
    fhand=open(fname,'r')
except:
    print("Enter proper file name with proper file-extension.(File name is case-sensitive)")
    quit()
s=fhand.read()
print("Number of words=",len(s.split()))
