#python function with no argument and bo return value

# def adding():
#     a=20
#     b=30
#     sum=a+b
#     print("after calling the function:",sum)
# adding()

  #global variable  

# y=20
# def sum():
#     global y
#     y=y+2
#     a=10
#     print (a)
# print(y)
# sum()
# print(y)    


#local variable # global variable

# y=10
# def add():
#     z=20
#     def inner():
#         nonlocal z
#         z=z+1
#         a=10
#         print(a)
#     print(z)
#     inner()
#     print(z)  
# add()              
        

#inner
# def inner():
#     x=4
#     print(x)
# inner() 



#lamda function
# a=10
# b=20
# sum-=lambda a,b:a+b
# diff=lambda a,b:a-b
# mul=lambda a,b:a*b
# div=lambda a,b:a/b
# print(sum(10,20))
# print(diff(10,20))
# print(div(10,20))
# print(mul(10,20))


#map function

# a=[1,2,3,4]
# a=map(lambda a: a+2, a)
# print(list(a))

#fliter
# a=[1,2,3,4]
# a=filter(lambda a: a%2==0,a)
# print(list(a))


#reduce
# from functools import reduce
# a=[1,2,3,4,5]
# b=reduce((lambda x,y:x+y),a)
# print(b)


#random function
#import random
# import random
# a=[1,2,3,4,5]
# print(random.choice(a))

# import math as a 
# print(a.factorial(5))

import  math as a
print(a.floor(-5.5))

# import math as a
# print(a.ceil(-5.6))











