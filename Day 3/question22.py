#print the element in the particular k index
my_list=(input( ))
k=int(input())
for i in range(my_list):
     print(k%len(my_list))      
     break    

idx=k%len(my_list)
print(my_list[idx])