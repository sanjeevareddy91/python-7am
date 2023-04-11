# Function : Set of line of code which performs a specific task..

# main feature of function is code reusuablility..

# a=43
# b=12

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# a=42
# b=15

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# declare a function follow belowe syntax:

# def -- it is the keyword for functions

"""
def function-name():
    statements
"""
# a=43
# b=12

# def arth_ops():
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)

# # calling of the declared function is mandatory..

# arth_ops()
# a=54
# b=23
# arth_ops()

# print(a)
# print(b)

# def arth_ops(a,b):
#     print(b)
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)

# arth_ops(32,33)

# print(a)
# print(b)

# passing the arguments to the function:
    # 1) Positional arguments
    # 2) Default arguments
    # 3) Keyword arguments
    # 4) Arbitrary Positional arguments
    # 5) Arbitrary Keyword arguments


# positional arguments: 
    # Assigning the values to the varibales is based on the position of the arguments.
# def emp_info(name,email,mobile):
#     print(f"Hi {name}, your email id is {email} and mobile number is {mobile} is updated in database")

# emp_info('suresh','suresh@gmail.com',8938364321)

# emp_info('mahesh','mahesh@gmail.com',9383376543)

# emp_info('venkatesh@gmail.com','93983939933','venkatesh')


# Default arguments:
    # Passing aa default value to the argument at the function declaration itself.
        # if value is passed during function call, default will be overridden or else default value will be considered..
# def emp_info(name,email,location='bangalore',mobile=63737337):
#     print(f"Hi {name}, your email id is {email} and mobile number is {mobile} and work location is {location} is updated in database")

# emp_info('suresh','suresh@gmail.com',8938364321,'hyderabad')

# emp_info('suresh','suresh@gmail.com','hyderabad')

# emp_info('suresh','suresh@gmail.com',8938364321)

# order of passing the value to the argument is very important..

# keyword arguments:
    # Passing values to the arguement based on the key-name at function call..

def emp_info(name,email,location,mobile):
    print(f"Hi {name}, your email id is {email} and mobile number is {mobile} and work location is {location} is updated in database")

emp_info(email="suresh@gmail.com",name='suresh',mobile='783383838',location='hyderabad')


emp_info(mobile='783383838',location='hyderabad',email="suresh@gmail.com",name='suresh')


# emp_info('suresh','suresh@gmail.com',mobile='7373383',location='bangalore')

# emp_info('venkatesh',name='mahesh',location='mumbai',mobile='839383938')

# emp_info(name='mahesh','suresh@gmail.com',location='mumbai',mobile='839383938')



# higher order function: Function calling other function inside it..

# Recursion : A function calling itself...


# n! = n*(n-1)!
# 6! = 6*5!
#      6*5*4!
#      6*5*4*3!
#      6*5*4*3*2!
#      6*5*4*3*2*1!
#      6*5*4*3*2*1*1 -- 720  

# def fact_cal(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n*fact_cal(n-1) # 6*5*4*3*2*1
    
# print(fact_cal(6))


# Lambda or Anonymous function: A function which doesnot have any name..

# Syntax:
    # lambda -- this is the keyword for lambda funcitons..
    # lambda arguments:expression


c = lambda a,b : a*b 


print((lambda a,b : a*b)(3,4))
print(c(3,4))


a = [54,88,43,67,42,65,19,16]


# map -- 
# print(list(map(lambda i:i-5,a)))



# filter -- 

# print(list(map(lambda i:i%2==0,a)))

# print(list(filter(lambda i:i%2==0,a)))

"""

Input:::
dict={
    "asaa":'asaa',
    "fsaf":"fsaf",
    "gagd":{
        "data":"data",
        "value":"value",
        "info":{
            "conpress":"compress",
            "product":"product",
            "data1":{
                "goon":"goon"
            }
        }
    },
    "sample":"sample"
    
}"""

"""
Output::
dict={
    "ASAA":'asaa',
    "FSAF":"fsaf",
    "GAGD":{
        "DATA":"data",
        "VALUE":"value",
        "INFO":{
            "COMPRESS":"compress",
            "PRODUCT":"product",
            "DATA1":{
                "GOON":"goon"
            }
        }
    },
    "SAMPLE":"sample"
    
}"""
