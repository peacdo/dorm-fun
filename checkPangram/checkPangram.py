# REJECTED, TRY AGAIN... 14.12.2023
# REJECTED, TRY AGAIN... 15.12.2023
x=input("Metin Girin :")
x=x.upper()
z=0
y=("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for m in range(26):
    for n in range(len(x)):
        if x[n]==y[m]:
            m=m+1
            z=z+1
            

if z >= 26 :   
    print("This is a pangram")
else : 
    print("This is not a pangram")

    #AAAAAAAAAAAAAAAAAAAAAA
