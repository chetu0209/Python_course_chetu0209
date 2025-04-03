#dictionaries
#dictionaries are unordered mappings for storing objects. Previously we saw how lists store objects in an ordered sequence, dictionaries use a key-value pairing instead.
#This key-value pair allows users to quickly grab objects without needing to know an index location.
#Dictionaries use curly braces and colons to signify the keys and their associated values. {key1:value1,key2:value2}

meanings= {"bat":"used to hit" , 
           "ball":"used to play cricket",
           "wicket":"used to bowl"
           }

print(meanings)
meanings["chethan"] ="02-09-2002"
print(meanings.get("cat","not found")) #if the key is not found it will return the value specified in the second argument
print(meanings)

x=meanings.pop("bat")
print(meanings)

del meanings["ball"]
print(meanings)

print(meanings.keys()) #prints all the keys
print(meanings.values()) #prints all the values
print(meanings.items())#prints all the items

#list of dictionaries
item1={"name":"milk",
       "weight":2,
       "price":50
       }
item2={"name":"bread",
         "weight":1,
         "price":30
         }
print(f"total price is {item1['price']+item2['price']} rs")


