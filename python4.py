#1.Write a program to print "Hello Data Science" 10 times using a loop.
'''
name="Hello Data Science"
for i in range(1,11):
    print(name)
'''
#2.Write a program to print numbers from 1 to N.
'''
num=int(input("enter the value:"))
for i in range(1,num+1):
    print(i)
'''
#3.Write a program to print numbers from N to 1.
'''
num=int(input("enter the value:"))
for i in range(num,0,-1):
    print(i)
'''
#4.Write a program to print all even numbers between 1 and N.
'''
even=int(input("enter the num:"))
for i in range(1,even+1):
    if i%2==0:
        print(i)
'''
    
#5.Write a program to print all odd numbers between 1 and N.
'''
even=int(input("enter the num:"))
for i in range(1,even+1):
    if i%2!=0:
        print(i)
'''
#Write a program to find the sum of the first N natural numbers.
        
#6Write a program to find the factorial of a number.
'''
num=int(input("enter the num"))
fact=1
for i in range (1,num+1):
    fact=fact*i
    print(fact)
'''
#7Write a program to print the multiplication table of a given number.
'''
num=int(input("enter the table:"))
for i in range(1,11):
        print(i,"*",num,"=",i*num)
'''

#8Write a program to count the number of digits in a number.
'''
digit=int(input("enter the num"))
i=0
for i in digit:
    i+=1
    print(i)
'''

#9Write a program to reverse a number.
'''    
rev=[1,2,3,4,5,6]
rev2=[34567]
rev.reverse()
print(rev)
rev2.reverse()
print(rev2)
num=int(input("enter the value:"))
num.reverse()
print(num)
'''
#10.Check whether a number is positive, negative, or zero.
'''
num=int(input("enter the num"))
if num>0:
    print("it is positive num")
elif num<0:
    print("it is negative")
else:
    print("it is zero")
'''
#11.Check whether a number is even or odd.
'''
num=int(input("enter the value"))
if num%2==0:
    print("it is even")
else:
    print("it is odd")
'''
#12.Find the largest among three numbers.
'''
num1=int(input("enter the num1:"))
num2=int(input("enter the num2:"))
num3=int(input("enter the num3:"))
if num1>num2 and num1>num3:
    print("lardest num of first num")
elif num2>num3 and num2>num1:
    print("lardest num of second num")
else:
    print("lardest num of thrd num")
'''
#13.Check whether a year is a leap year.
'''
num=int(input("enter the year"))
if num%400==0  and num%4==0 and num%100!=0:
    print("it is leap year")
else:
    print("not leap year")
'''
#14,Create a simple calculator using if-elif-else.
'''
print("choice your calculator opertor")
print("1.add")
print("2.sub")
print("3.div")
print("4.multi")
num1=int(input("enter the num value:"))
num2=int(input("enter the num value:"))
select=int(input("enter your choice:"))
if select==1:
    add=num1+num2
    print("add",add)
elif select==2:
    sub=num1-num2
    print("sub",sub)
elif select==3:
    if num2!=0:
        div=num1/num2
        print("div",div)
    else:
        print("can not divide by zero")
elif select==4:
    multi=num1*num2
    print("mulit",multi)
else:
    print("invalid")
'''
#15Check whether a number is divisible by both 5 and 11.
'''
num=int(input("enter the num:"))
if num%5==0 and num%11==0:
    print(num,"is divied by both 5 and 11")
else:
    print("not divied by both 5 and 11")
'''
#16Assign grades based on student marks.
'''
std=int(input("enter the mark:"))
if std>=90 and std<=100:
    print("student grades is O:",std)
elif std>=80 and std<90:
    print("student grades is A+:",std)
elif std>=70 and std<80:
    print("student grades is A:",std)
elif std>=60 and std<70:
    print("student grades is B+:",std)
elif std>50 and std<60:
    print("student grades is B:",std)
elif std>=45 and std<=50:
    print("boder pass",std)
else:
    print("fail")
'''
#17Check whether a character is a vowel or consonant.
#18Check whether a person is eligible to vote.
'''
age=int(input("enter the age"))
if age>=18:
    print(" you eligible to vote.")
else:
    print("note eligible to vote")
'''
#19Find the smallest among three number.
num1=int(input("enter the num1:"))
num2=int(input("enter the num2:"))
num3=int(input("enter the num3:"))
if num1<num2 and num1<num3:
    print("smallest num of first num:",num1)
elif num2<num3 and num2<num1:
    print("smallest  num of second num:",num2)
else:
    print("smallest num of thrd num:",num3)



















































































