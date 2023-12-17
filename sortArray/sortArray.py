x=int(input("Enter the length of the array :"))
l=list()

for n in range(1,x + 1):
    a=int(input(f"Enter the element #{n} :"))
    l.append(a)



for n in range(len(l)):
    for i in range(n,len(l)):
        if l[n]>l[i]:
            temp=l[n]
            l[n]=l[i]
            l[i]=temp
            print(l)
    






#listedeki eleman sayısı x'e kadar
# 30 20 10