def great():
    print("Hello, this is a function")
    return 5

great()
great()

def add(a, b):
    return a + b
a=5
b=10
result = add(a, b)
print(result)

def tables(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

tables(5)
tables(10)

def func():
    x ="chethan"
    print("hello world")
    
 # variable-length arguments
def add(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add(1, 2, 3, 4, 5)) # returns 15

print(add(10, 20, 30)) # returns 60   

# keyword arguments
def student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

student_info(name="John", age=20, city="New York")
student_info(name="Alice", age=25, country="USA")

# lambda function
add = lambda x, y: x + y
print(add(5, 10))

students = [
    {"name": "John", "age": 20},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 22}
]
students.sort(key=lambda x: x["age"], reverse=True)
print(students) 

# recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5)) 


def calculate(a,b):
    def sub():
        print(a-b)
    def add():
        print(a+b)
    def mul():
        print(a*b)
    add()
    sub()
    mul()

calculate(10,5)

