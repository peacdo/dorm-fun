x=input("Metin Giriniz :");y=("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz")

def func():
    z=0
    for m in range(len(x)):
        for n in range(52):
            if x[m]==y[n]:
                z=z+1
                break
            
    if z == len(x):
        print("he")
    else:
        print("yok") 
               
func()