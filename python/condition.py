# Python Conditions and If statements
# Python supports the usual logical conditions from mathematics:
#     Equals: a == b
#     Not Equals: a != b
#     Less than: a < b
#     Less than or equal to: a <= b
#     Greater than: a > b
#     Greater than or equal to: a >= b


a=10
b=3
if a==b:
    print ("both are equal and result is zero:",a-b)
else :
    print("not equals")


def fun(a,b):
    if a==b:
        print("both are equal")
    else:
        print ("not equal")
one=int(input("enter first number:"))
two=int(input("enter second number:"))
fun(one,two)
