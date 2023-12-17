# rejected 17.12.2023
# rejected again 17.12.2023
# rejected yet again 17.12.2023

snum=str();sname=str();ssname=str();syob=str();l=["\nList of recorded students :\n"] 
def mainLoop():
    x=input("\nChoose an operation(type -h for help): ")
    y=x.split(" ")
    z=y[0]
    match z :
        case "-h":
            print("""
                -add: add record (-add [student_number], [student_name], [student_surname], [student_year_of_birth])
	        -del: delete record (-del [student_number])
	        -dellall: delete all records (-delall)
	        -show: display a single record (-show [student_number])
	        -showall: display all records (-showall)
	        -exit: exit session (exit and display everyting recorded in this instance)
            """)
            return mainLoop()
        case "-add":
            x=x.replace("-add","")
            if len(x)<8 :
                print("\nYou may want to write the number, name, surname, and year of birth of student that you want to add to system.\n (-add [student_number], [student_name], [student_surname], [student_year_of_birth])")    
                return mainLoop()
            a,b,c,d=x.split(",")
            for i in range(1,len(l)):
                k=l[i].split(",")
                j=k[0]
                if a == j :
                    print("\nThis student allready recorded.") 
                    return mainLoop()
            addRecord(a,b,c,d)
            print("\nStudent has been recorded to system.")
            return mainLoop()
        case "-del":
            p=False
            x=x.replace("-del","")
            if len(x) < 1 :
                print("\nThere is no student has that number in the system.\n(-del [student_number])")
                return mainLoop()
            
            for i in range(1,len(l)):
                k=l[i].split(",")
                j=k[0]
                if x == j :
                    p=True
                    l.remove(l[i])
                    print(f"\nStudent who has the number '{x}' has been deleted from the system.")
                    break
            if p==False:
                 print("\nThere is no student has that number in the system.\n(-del [student_number])")
            return mainLoop()          
        case "-delall":
            delall()
            print("\nAll records have been deleted.")
            return mainLoop()
        case "-show":
            p=False
            x=x.replace("-show","")

            if len(x) < 1 :
                print("\nThere is no student has that number in the system.\n(-show [student_number])")
                return mainLoop()
            
            for i in range(1,len(l)):
                k=l[i].split(",")
                j=k[0]
                if x == j :
                    p=True
                    print("\n",l[i])
                    break
            if p==False:
                 print("\nThere is no student has that number in the system.\n(-show [student_number])")
            return mainLoop()           
        case "-showall":    
            showall()
            return mainLoop()
        case "-exit":
            showall()
            return print("\t\nHave a nice day...")
        case _ :
            print("\nInvalid operation.You may want to check help.")
            return mainLoop()       
def dell(x):
    
    for i in range(1,len(l)):
        if x in l[i]:
            l.remove(l[i])
def delall():
    l=[]
    l.append("\nList of recorded students :\n")
    return l    
def showall():
    print(l[0])
    for n in range(1,len(l)):
                print("\n",f"#{n}",l[n],"\n")
def addRecord(snum,sname,ssname,syob): 
    record= f"{snum},{sname},{ssname},{syob}"
    l.append(record)    
mainLoop()
#1: odtu231224, Sertaç ,Kandemir, 2006
#2: hacettepe38, Semih Buğra, Kartın, 2005
#3: gazipedo109, Yasin, Gülhan, 2010 
#-add 1,2,3,4