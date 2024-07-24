#print the next coming four letters with the addition of 4 EXAMPLE ABC GIVES DEF
s=input()
n=int(input())
for i in s:
    e=ord(i)+n
    print(chr(e),end="")