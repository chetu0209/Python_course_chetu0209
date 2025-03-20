#lists

items = ["apple", "banana", "cherry","banana"]
print(items)
print(items[1])
items.pop()
print(items)
items.pop(2)
print(items)
items.append("orange")
print(items)
items.remove("apple")
print(items)
items.insert(1, "grapes")
print(items)
items[1]="kiwi"
print(items)
print(items.count("banana"))
items.reverse()
print(items)
items.sort()    #sorts in ascending order
print(items)
items.sort(reverse=True)    #sorts in descending order
print(items)

matrix =[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print(matrix[1][1])


item=[1,3,4,5]
print(item)
item.append(6)
print(item)
item.insert(1,2)
print(item)
item.remove(3)
print(item)

item=[1,5,2,4,3]
item.sort(reverse=True)
print(item)
item.reverse()
print(item)

