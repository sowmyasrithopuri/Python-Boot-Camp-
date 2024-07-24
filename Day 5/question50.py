#print the numeric values of the given string and add them
c=['a','e','i','o','u']
abc="bcdfghjklmnpqrstvwxyz"
check="0123456789"
ans=0
i="hello 1234world"
inp=i.lower()
for i in inp:
    if(i  in check):
        ans+=int(i)
print(ans)

#reverse the numbers present in the string

