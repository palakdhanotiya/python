#check age
"""age=int(input("enter age: "))

if(age>21):
    print("can marry")
elif(age>=18 and age<21):
      print("Yes, not a child,so can marry but not legally")
else:
   print("cant marry")"""
   
#check tarffic light

"""light=input("show tarffic light:")

if(light=="red"):
    print("STOP")
elif(light=="green"):
    print("GO")
elif(light=="yellow"):
    print("LOOK")
elif(light=="blue"):
    print("Light is Broken")
else:
    print("invalid color")"""

#check grade
"""marks=int(input("marks: "))
if(marks >= 90 and marks <= 100):
    print("grade A")
elif(marks>=80 and marks <90):
    print("grade B")
elif(marks>=70 and marks <80):
    print("grade C")
elif(marks>=35 and marks <70):
    print("grade D")
else:
    print("FAIL")"""

#print output
#A=5 & G=M______A=2 & G=F

"""A= int(input("A: "))
G= input("M/F: ")

if((A==1 or A==2) and G=="M"):
    print("fee is 100")
elif(A==3 or A==4 or G=="F"):
    print("fee is 200")
elif(A==5 and G=="M"):
    print("fee 300")
else:
    print("no fee")"""


#---------Ternary Opreator----------
#Single if 

"""food=input("food: ")
eat="YES" if food =="cake" else "NO"
print(eat)

dessert=input("dessert:")
print("sweet") if dessert=="cake"or dessert=="jalebi" else print("sour")"""

#clever if




#Question
a=[1,2,3,4]
b=[10,20,30]
c=[]
for x,y in zip(a[1:],b):
    c.append(x-y)
    print(c)