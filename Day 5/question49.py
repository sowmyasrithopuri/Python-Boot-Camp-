
#print the unique characters in a given string
check=['a','e','i','o','u']
abc="bcdfghjklmnpqrstvwxyz"
ans=" "
i="hello world"
inp=i.lower()
for i in inp:
    if(i  not in ans):
        ans+=i
print(ans)