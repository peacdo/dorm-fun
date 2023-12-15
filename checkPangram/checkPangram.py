# REJECTED, TRY AGAIN... 14.12.2023
# Online Python-3 Compiler (Interpretex
x=input("Metin Girin :")
x=x.upper()
z=0
y=("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for m in range(26):
    for n in range(len(x)):
        if x[n]==y[m]:
            z=z+1
            

if z >= 26 :   
    print("he")
else : 
    print("yok")
