stairs=int(input("How many stairs do you want to climb: "))
single=stairs
double=0
way_count=0
result=0

def factorial(x):
    for i in range(1,x):
       x*=i
    if x == 0 :
        x=1
    return x

while True:
    if double*2 > stairs:
        break
            
    result+=factorial(stairs-way_count)/(factorial(single)*factorial(double))

#    for i in range(single):
#        print("1 step",end=" + ")
#    
#    for i in range(double):
#        print("2 step",end=" + ")

    single-=2    
    double+=1

#    print("")
    way_count+=1

print("\n\t",f"""Assuming you can climb 1 or 2 steps at a time
           You can climb this stairs in {int(result)} ways\n""")


# 1 step + 1 step + 1 step + 1 step 4!/(4!*0!)
# 1 step + 1 step + 2 step          3!/(2!*1!)
# 2 step + 2 step                   2!/(0!*2!)