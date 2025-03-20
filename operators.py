#operators
#Assignment operators
a=10
a+=100
print(a)

#comparison operators
a=10
b=20
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#logical operators
print(1>2 and 2>1)
print(1>2 or 2>1)
print(not 1>2)

#membership operators
a="hello"
print('h' in a)
print('h' not in a)

a="chetu"
a1="chetusp"
print(("c" in a)and("c" in a1))
print(("p" in a)or("p" in a1))
print("p" not in a)

#bitwise operators
a=5 #101
b=3 #011
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a<<2)
print(a>>2)

a=input("Enter a number")
a=int(a)
b=input("Enter a number")
b=int(b)
print(a>10 and b>10)
print(a<5 or b<5)
print(not a>b)

a=input("Enter your age:")
a=int(a)
if(a>=18):
    print("you are an adult")
else:
    print("you are a minor")


a="chethan"
print("h" in a)
print("s" not in a)


a=10 #1010
b=20 #10100
print(a&b)
print(a|b)
print(a^b)
print(a<<2)
print(b>>2)

