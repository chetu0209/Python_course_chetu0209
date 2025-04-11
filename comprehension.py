l = [1,23,43,53,67]
total = 0
for i in l:
    print(total)
    total += i
print(total)
print("\n")

l = [1,23,43,53,67]
dl = []
for i in l:
    dl.append(i*2)
    print(dl)

student_marks = {"chetu": 100, "spoorthi": 90, "rohit": 80}

for student, marks in student_marks.items():
    print(f"{student}---{marks}")
print("\n")

students =["chetu", "spoorthi", "rohit"] 
marks = [80, 100, 40]  

student_marks = {}

for i in range(len(students)):
    student_marks[students[i]] = marks[i]
print(student_marks)

l = [1, 2, 3, 4, 5]
dl = [i*2 for i in l]
print(dl)
print("\n")

l = [x for x in range(1,11)]
print(l)
dl = [x**2 for x in l if x%2==0]
print(dl)

names = ["chetu", "spoorthi", "rohit"] 

d={name:len(name) for name in names}
print(d)

#List input practice

x=[int(num) for num in input("enter list of numbers: ").split() ]
print(x)