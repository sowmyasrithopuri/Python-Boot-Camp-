#ascii questions from 38 to42
for i in range(32,128):
   print(chr(i),end=" ")

inp=input()
count=0
for i in(inp):
    if (ord(i)>=48 and ord(i)<=57):
      count+=int(i)
print(count)