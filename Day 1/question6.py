#according to the previos history z participated in 14 games out of that he won
#write a program to check whether z,x,y travel in same plane or not

bh=int(input("height of x: "))
bw=int(input("weight of x: "))
th=int(input("height of y: "))
tw=int(input("weight of y: "))
fact7=(50*14)/100
if(bh==140 and bw%2==0):
    print("mr x is selected for badminton")
elif(th<140 and th>118 and tw%fact7==0):
    print("mr y is selected for table tennis")
else:
    print("mrz is selected for swimming")