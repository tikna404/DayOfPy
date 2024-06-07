import math
def leap(n):
    if(n%400==0 and n%100==0):
        c=1
    elif(n%4==0 and n%100!=0):
        c=1
    else:
        c=2
    return c
def day(n):
    c=0
    for i in range(0,n):
        if(i%2==0):
            c+=31
        if(i%2!=0):
            c+=30
    return c
def cal(year,days):
    c=0
    s=""
    k=math.floor(days/367*12)
    if(k>7):
        c=day(7)
        c+=day(k-7)
    else:
        c=day(k)
    if(k>2):
        c=c-leap(year)
    s=str(days-c)+"."+str(k+1)+"."+str(year)
    return s
    
y=int(input("Enter Year:"))
d=int(input("Enter nth day of the year:"))
print(cal(y,d))
    