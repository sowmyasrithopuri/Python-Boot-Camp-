#find the element present in k+N index

my_list=list(map(int,input().split()))
k=int(input())
n=int(input())
t=k+n
if(len(my_list)<k+n):
    print("error")
else:
   for i in range(len(my_list)):
          print(my_list[t])
          break
   

