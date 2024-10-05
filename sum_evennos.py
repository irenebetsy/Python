r=int(input("Enter Range:"))
a=0
for i in range(1,1+r):
    if i%2!=0:
        a=a+i
    else:
        continue
print(a)