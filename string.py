# Date: 11/10/2019

age = input("Age:")
print(age)

boy_name = input("Boyname:")
boy_age = int(input("Boyage:"))
girl_name = input("Girlname:")
girl_age = int(input("Girlage:"))

age_diff = abs(boy_age - girl_age)
print(f"{boy_name} loves {girl_name}. Age dissimilarity is {age_diff}.")
