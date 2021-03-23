print("Enter 2 numbers")


try:
    a=int(input("Enter a:\t"))
except:
    print("Enter digits")
    exit()



try:
    b=int(input("Enter b:\t"))
except:
    print("Enter digits")
    quit()


print("Sum is",a+b)
