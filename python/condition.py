# Python Conditions and If statements
# Python supports the usual logical conditions from mathematics:
#     Equals: a == b
#     Not Equals: a != b
#     Less than: a < b
#     Less than or equal to: a <= b
#     Greater than: a > b
#     Greater than or equal to: a >= b


# a=10
# b=3
# if a==b:
#     print ("both are equal and result is zero:",a-b)
# else :
#     print("not equals")


# def fun(a,b):
#     if a==b:
#         print("both are equal")
#     else:
#         print ("not equal")
# one=int(input("enter first number:"))
# two=int(input("enter second number:"))
# fun(one,two)


# def fun(a,b):
#     if a!=b:
#         print("a is not equal b")
#     else:
#         print("equal")
# one=int(input("enter first number:"))
# two=int(input("enter second number:"))
# fun(one,two)

# Short Hand If
# If you have only one statement to execute, 
# you can put it on the same line as the if statement.
# a=5
# b=3
# if a > b:print("hello mim")

def fun(a,b):
    print ("i love you mim") if a>b else print("jaf love mim")
one=int(input("enter first number:"))
two=int(input("enter second number:"))
fun(one,two)
