#write a program to print all the consonants


check=['a','e','i','o','u']
abc="bcdfghjklmnpqrstvwxyz"
count=0
c=0
i="hello world"
inp=i.lower()
for i in inp:
    if(i in abc):
         count+=1
print(count)