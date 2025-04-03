# while loop

i=0
while i<=10:
    x=0
    while x<i:
        print("*",end="_")
        x+=1
    print("")
    i+=1
    
pin =1234
attempts = 0
while attempts <3:
    user_input = int(input(f"Attempts-{attempts}:"))
    if user_input == pin:
        print("Access granted")
        break
    else:
        print("Incorrect pin")
        attempts += 1