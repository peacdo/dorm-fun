# REJECTED, TRY AGAIN... 14.12.2023
# REJECTED, TRY AGAIN... 15.12.2023
# REJECTED, TRY AGAIN... 16.12.2023

x=input("Metin Girin :")
x=x.upper()
z=0
m=0
y=("ABCDEFGHIJKLMNOPQRSTUVWXYZ/")

for a in range(26) :
    n=0
    for n in range(len(x)):
        if x[n]==y[m]:
            y=y.replace(y[m],"")
            z=z+1
                   
            
if z >= 26 :   
    print("This is a pangram")
else : 
    print("This is not a pangram")