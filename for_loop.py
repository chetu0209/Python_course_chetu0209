
for i in range(1, 11):
    print(i, end="  ")

print("\n")
bag = ["red", "green", "blue", "yellow"]
for ball in bag:
    print(ball)

for i in range(1, 11, 2):
    print(i, end="  ")
print("\n")

name = "Chethan"
for index, char in enumerate(name):
    print(char*(index+1))
print("\n")

l = [1, 2, 3, 4, 5]
for index, value in enumerate(l):
    print(f"Index: {index}, Value: {value}")
print("\n")

d = {"name": "Chethan", "age": 25, "city": "Bangalore"}
for key, value in d.items():
    print(f"{key}: {value}")
print("\n")

for i in range(1, 11):
    print(f"2x{i} = {2*i}")
print("\n")

#nested for loop to print multiplication table
for i in range(2, 11):
    for j in range(1, 11):
        print(f"{i}x{j} = {i*j}")
    print("\n")




 