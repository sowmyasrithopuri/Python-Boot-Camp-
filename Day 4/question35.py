year1=int(input("enter the year"))
year2=int(input("enter the year"))
for i in range(year1,year2+1):
         if year1%400==0 or (year1%4==0 and year1%100!=0):
           print(i)