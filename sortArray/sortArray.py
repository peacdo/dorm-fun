x=int(input("Enter the length of the array :"))
lst=list()

for n in range(1,x + 1):
    a=int(input(f"Enter the element #{n} :"))
    lst.append(a)

def döngü():
    for n in range(len(lst)):
        for m in range(n,len(lst)):
            if lst[n] > lst[m]:
                lst.insert(m+1,lst[n])
                lst.pop(n)
                print(lst)
                
                
döngü()
print(lst)





#listedeki eleman sayısı x'e kadar
# 30 20 10