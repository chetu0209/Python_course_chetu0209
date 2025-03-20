#Tuples

genders=("male","female","other")
print(genders.index("male"))

#Sets
s={20,2,123} #set is unordered and unindexed
print(s)
#print(s[1]) #sets are unindexed 
s2=set ((1,2,3))
print(type(s2))

s1={1,2,3}
s2={3,4,5}
print(s1 |s2) #union
print(s1 & s2) #intersection
print(s1 - s2) #difference

s1.add(4)
print(s1)
#s.remove(10) #remove will give error if element is not present
#s.discard(10) #discard will not give error if element is not present
s1.pop() #removes random element
print(s1)
s1.clear() #clears the set
print(s1)



