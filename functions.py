'''def calc_sum(a,b):
    s=a+b
    return s

print(calc_sum(8,97))
calc_sum(12,17)
calc_sum(18,11)'''

'''def hello():
    print("hello")

output=hello()
print(output)'''


#average of 3
'''def average_3(a,b,c):
    return a+b+c/3

print(average_3(4,8,10))'''

#average of 5
'''def average_5():
    c = int(input("enter c marks:"))
    python= int(input("enter python marks:"))
    java= int(input("enter java marks:"))
    html= int(input("enter html marks:"))
    css= int(input("enter css marks:"))
    total_marks = c+python+java+html+css
    final_precentage = total_marks/5
    print(final_precentage)
    

average_5()
'''

#print  length of a list
'''cities = ["indore","udipur","jaipur","mumbai","vrindavan"]
states= ["rajasthan","aasam","sikhim","tamilnadu"]
counteries = ["japan","singapure","canda","egypt","italy"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(states)
print_len(counteries)'''

#print elements of list in single line(list is parameter)
'''ipl_teams= ["RCB","MI","CSK","SRH","GT","DC","KKR"]

def print_list(list):
    for item in list:
        print(item,end= " ")

print_list(ipl_teams)'''

#find the factorial of n.(n is the parameter)

'''def fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

fact(6)'''

#convert USD to INR
'''def convert_dollar(n):
    inr_val= n*83
    print(n, "USD=",inr_val,"INR")

convert_dollar(11)'''

#input number print even odd

def even_odd(n):
    if(n%2==0):
        print("EVEN")
    else:
        print("ODD")

even_odd(6)