import datetime
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
def date(y,m):
    c=0
    if(m>7):
        c+=day(7)
        c+=day(m-7)
    else:
        c+=day(m)
    if(m>1):
        c=c-leap(y)
    return c
        
def cal(s):
    today = str(datetime.date.today()).split("-")
    cy,cm,cd=int(today[0]),int(today[1]),int(today[2])
    pd,pm,py=int(s[0]),int(s[1]),int(s[2])
    c=0 #367days
    for i in range(py,cy):
        c+=leap(i)
    k=(cy-py)*367-c
    p=date(py,pm-1)+pd
    t=date(cy,cm-1)+cd
    print(k-p+t,"days")
    
s=input("Enter in dd.mm.yyyy:")
s=s.split(".")
cal(s)
