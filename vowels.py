string=input("Enter a string:")
vowels='a','e','i','o','u'
list_str=list(string.lower())
ans=[]
for i in list_str:
    if i in vowels:
        ans.append(i)
answer=''.join(ans)
print(answer)