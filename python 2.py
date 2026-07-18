# data type
'''
b=49
c=90.0
d="apple"
print(type(b))
print(type(c))
print(type(d))
print(type(b))
'''
'''
name=input("enter the name:")
age=int(input("enter the age:"))
salary=int(input("ente the salary:"))
print(type(name))
print(type(age))
print(type(salary))
'''
'''
a=200
b=float(a)
print(type(b))
'''
'''
a=90.0
b=int(a)
print(type(b))

c="49"
d="1"
convet1=int(c)
convet2=int(d)
add=convet1+convet2
print(add)
'''
'''
update=int(input("enter the update value:"))
update+=300
print("updateing value",update)
reduce=int(input("enter the reduce value:"))
reduce-=300
print("reducing value",reduce)
double=int(input("enter the double the salary:"))
double*=10000
print("double",double)
remain=int(input("enter the value:"))
remain%=4
print("store the remainder value",remain)
'''
#dynamic typing
'''
a=46.89
a="deepi"
a=59
print(a)
'''
'''
a="5678"
b=int(a)
print(type(b))

x=90
print(x)
x=56
print(x)
x=67
print(x)
x=62
print(x)
x=45
print(x)
'''
#arithmetic operators
'''
print("1.add")
print("2.sub")
print("3.multiple")
print("4.divien")
choice=int(input("enter  the choic:"))
a=int(input('enter the value:'))
b=int(input("enter the value:"))
if choice=="1":
      print("add",a+b)
elif choice=="2":
    print("sub",a-b)
elif choice=="3":
    print("multiple",a*b)
elif choice=="4":
    print("divistion",a/b)
else:
    print("invalid")
'''
'''
w=int(input("enter the with:"))
l=int(input("enter the lenght:"))
print("area idf rectangle",w*l)
r=int(input("enter the r:"))
circle=2*3.14*r
print ("perimeter of circle",circle)
'''
'''
sub1=int(input("enter the mark"))
sub2=int(input("enter the mark"))
sub3=int(input("enter the mark"))
sub4=int(input("enter the mark"))
sub5=int(input("enter the mark"))
total=(sub1+sub2+sub3+sub4+sub5)/5
print("your aveage mark",total)
'''
#assignment operator
'''
a=68
a+=2
print(a)
b=56
b-=5
print(b)
c=89
c*=2
print(c)
d=8
d//=2
print(d)
e=9
e%=2
print(e)
'''
#comparision operators
'''
num1=int(input("enter the num1:"))
num2=int(input("enter the num2:"))
if num1==num2:
    print("num1 and num2 equal")
'''
'''
num1=int(input("enter the num1:"))
num2=int(input("enter the num2:"))
if num1>num2:
    print("first num is greater than num2")
else:
    print("small num")
'''
'''
age=int(input("enter the age:"))
if age>18:
        print("your age is above 18 :")
'''
'''
mark=int(input("enter the mark:"))
if mark>=50:
         print("your result is pass:")
else:
    print("your result is fail:")
'''
'''
salary=int(input("enter the your salary:"))
if salary>=50000:
   print("your salary is above 50000")
else:
    print(" your salary is below 50000" )
'''
#logical operator
'''
name=input("enter the name:")
password=int(input("enter the password:"))
if name=="deepika" and password==2005:
    print("your name and password valid")
else:
    print(invalid)
'''
'''
age=int(input("enter the age:"))
if age>=18:
    print("citizenship")
'''
'''
tem=int(input("enter the tem:"))
if tem>=20 or tem>=30:
    print("normal")
else:
    print("heay")
'''
'''
a=input("enter the email:")
b=int(input("enter the password:"))
if a=="deepi@gmail.com" or b==1234:
    print("login")
    print("valid")
else:
    print("invalid")
'''
#identotiy operators
'''
a=["a","b","c","d"]
c=a
print(c is a)
b=["1","2","3","4"]
a=b
print(a is not b)
e=["1","2","3","4"]
b=e
print (b is e)
'''
#string
'''
a="deepi"
print(a.upper())
b="I AM DEEPIKA ,DEPARTMENT OF AI&DS"
print(b.lower())
c="deepika"
print(c.reversed)
'''
#if statement
'''
num=int(input("entr the num:"))
if num%2==0:
    print("it is even")
else:
    print("it is odd")
'''
'''
num=int(input("enter the num:"))
if num>0:
    print("it is positive")
elif num==0:
    print("is rezo")
else:
    print("negative")
'''
'''
mark=int(input("enter the mark:"))
if mark>=60 and mark<70:
    print("grade B+")
elif mark>=70 and mark<80:
    print("grade A")
elif mark>=80 and mark<90:
    print("grade A+")
elif mark>=90 and mark<=100:
    print("grade O")
elif mark>=45 and mark <60:
    print("grade c")
else:
    print("fail")
'''
'''
ATM=input("enter the account name")
pin_num=int(input("enter the pin num:"))
if ATM=="deepika" and pin_num==9876:
    print("your balance 40000")
elif ATM!="deepika":
    print("your account name wrong")

    print("pleace enter corrt account name")
elif pin_num!=9876:
    print("your pin num wrong")
    print("enter corret pin num")
else:
    print("invalid")
'''
'''
color=input("enter color:")
if color=="green":
    print("go")
elif color=="red":
    print("stop your vechicles")
elif color=="yellow":
    print("start the vachicls")
else:
    print("only 3 color red,yellow,green")
'''
#else statement
'''
age=int(input("enter the your age:"))
if  age<=15:
    print("not eligibility")
else:
    print("eligility")
'''
'''
salary=int(input("enter the salary"))
if salary>=30000:
    print('eligitiy')
else:
    print("not eligibility")

num=int(input("enter the num:"))
if num%5==0:
    print("num divisibility by 5")
else:
    print("can not divisibility by 5")
'''
#nested if
'''
age=int(input("enter the age:"))
result_12th=input("enter the result:")
if age>=17:
    if result_12th=="pass":
        print("eligibility for collage addmisin")
    else:
        print("only pass std eligibily for clg addmision")

else:
    print("your age id beloe 17 not eligibility clg addmisson")
'''
#for loop
'''
for i in range(1,11):
    print(i)
'''
'''
num=int(input("enter the num;"))
for i in range(1,11):
    print( i,"*",num,"=",i*num)
'''
'''
for i in range(1,51):
    if i%2==0:
        print(i)
'''
'''
for i in range(1,5):
    for j in range(i):
        print("*",end=" ")
    print()
'''
'''
for i in range(1,21):
    if i%2==0:
        print(i)
'''
'''
for i in range(51,0,-1):
    if i%2==0:
        print(i)
'''

num=int(input("enter the num:"))
for i in range(num):
     if i%3==0:
         continue
     elif i%9==0:
         break
     else:
         print(i)


'''
num=int(input("enter the num:"))
for i in range(num,0,-1):
    if i==5:
        pass
    elif i<1:
        break
    print(i)
'''
'''
#nested for loop
for i in range(1,7):
    for j in range(7,1,-1):
        print("*",end="")
    print()

'''




































































     





























    
        
    






































































               
        





































        

            


































        
            
         

































































         
      
        

























































        
