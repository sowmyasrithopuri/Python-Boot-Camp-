#replace the elements in an array with average of min and max elements
my_list=list(map(int,input().split(" ")))
max=my_list[0]
min=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]<min):
        min=my_list[i]
print(min)
max=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]>max):
        max=my_list[i]  
print(max)
avg=(min+max)//2
print(avg)
for i in range(len(my_list)):
     my_list=avg
print(my_list)