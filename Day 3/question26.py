#find the missing element in array
my_list=list(map(int,input().split()))
k=sum(my_list)
print("sum of list:",k)
sum=0
n=int(input("enter the number"))
sum=(n*(n+1))//2
print(f"the sum of first {n} natural numbers is",sum)
print("missing number in the list is",sum-k)









