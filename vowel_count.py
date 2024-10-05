string=input("Enter a string:")
vowels='a','e','i','o','u'
list_str=list(string)
ans=[]
for i in string.lower():
    if i in vowels:
        ans.append(i)
    else:
        continue
print(len(ans))