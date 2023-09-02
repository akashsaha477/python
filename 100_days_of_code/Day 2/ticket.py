height=int(input("Whta is your height?"))
age=int(input("What is your age?"))
photo=input("Do you want photo? Y/N ")
pay=0
if height>=120:
    print("You can ride.")
    if(age>18):
        print("You are an adult")
        pay=12
    elif(age<12 and age>18):
        print("You are a teenager")
        pay=7
    else:
        print("You are a kid")
        pay=5
    if(photo=="Y"):
        pay+=3
        print(f"Your final bill is {pay}")
    elif(photo=="N"):
        print(f"Your final bill is {pay}")
else:
    print("You can't ride.")