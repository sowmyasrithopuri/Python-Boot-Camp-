#print all the vowels followed by consonants
check=['a','e','i','o','u']
abc="bcdfghjklmnpqrstvwxyz"
ans=" "
i="hello world"
inp=i.lower()
for i in inp:
    if(i in check):
        ans+=i
print(ans)

for i in inp:
    if(i in abc):
        ans+=i
print(ans)
