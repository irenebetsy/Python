r=int(input("Enter range:"))
pattern="*"
print(pattern)
for i in range(1,r):
    pattern=pattern+"*"
    print(pattern)

r=int(input("Enter range:"))
for i in range(1,r+1):
    for j in range(r-i):
        print(" ",end="")
    for k in range(1,2*i):
        print("*",end="")
    print()

r=int(input("Enter range:"))
for i in range(1,r+1):
    for j in range(r-i):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")
    print()

