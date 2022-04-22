age = input("Are you a cigarette addict older than 75 years old? ")
chronic = input("Do you have a severe chronic disease? ")
immune = input("Is your immune system too week? ")

if age == "Yes" or age == "yes" :
    age = True
else :
    age = False
if chronic == "Yes" or chronic == "yes" :
    chronic = True
else :
    chronic = False
if immune == "Yes" or immune == "yes" :
    immune = True
else :
    immune = False

if age or chronic or immune == True :
    print("You are in risky group")
else :
    print("You are not in risky group")