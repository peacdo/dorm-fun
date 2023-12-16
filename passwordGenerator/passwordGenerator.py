import random
password=str()
alphabet=("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
symbols=("!'^+%&/()=?_>£#$½{[]}\\|/*-+.:,;")
print("\t"*3,"Enter your preferences")

l=[]

 
lenght=int(input("Password Length: "))
num=int(input("How many password do you want to generate: "))



def checkPreferences():
    a1=input("Include Numbers: ")
    match a1 :
        case  "no":
            a1=bool(0)
        case "yes":
            l.append(1)
        case _ :
            print("\nPlease write only 'yes' or 'no'")
            print("\n")
            return checkPreferences()
    a2=input("Include Lowercase Characters: ")
    match a2 :
        case  "no":
            a2=bool(0)
        case "yes":
            l.append(2)
        case _ :
            print("\nPlease write only 'yes' or 'no'")
            print("\n")
            return checkPreferences()
    a3=input("Include Uppercase Characters: ")
    match a3 :
        case  "no":
            a3=bool(0)
        case "yes":
            l.append(3)
        case _ :
            print("\nPlease write only 'yes' or 'no'")
            print("\n")
            return checkPreferences()
    a4=input("Include Symbols: ")
    match a4 :
        case  "no":
            a4=bool(0)
        case "yes":
            l.append(4)
        case _ :
            print("\nPlease write only 'yes' or 'no'")
            print("\n")
            return checkPreferences()
    return l

checkPreferences()

def randomPasswords():
    password=""
    while len(password) < lenght :
        temp=random.choice(l)
        if temp == 1 :
            password=password+str(random.randrange(10))
        elif temp == 2 :
            password=password+alphabet[random.randrange(26)].lower()
        elif temp == 3 :
            password=password+alphabet[random.randrange(26)]
        elif temp == 4 :
            password=password+str(symbols[random.randrange(31)])
    return password

for n in range(1,num+1):
    print(f"#{n}:",end=" ")
    print(randomPasswords())
    