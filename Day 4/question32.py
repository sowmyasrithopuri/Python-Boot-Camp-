#sort elements and 1st half in ascending order and 2nd half in descending order
my_list=list(map(int,input("enter list elements").split(" ")))
length=len(my_list)
my_list.sort()
for i in range(length//2):
    print(my_list[i],end=" ")
for j in range(length-1,length//2-1,-1):
    print(my_list[j],end=" ")