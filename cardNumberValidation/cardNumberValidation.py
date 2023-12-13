num=input("Kredi Karti Numarasi Giriniz :")
len=len(num)
n=0

def secondDigitNums(n):
    temp1=0
    while  len-2-2*n >= 0 :
        if 2*int(num[len-2-2*n]) >= 10 :
            temp1=2*int(num[len-2-2*n]) % 10 +1+ temp1
        else :
            temp1=2*int(num[len-2-2*n]) + temp1
        n=n+1 
    return temp1

def singleDigitNums(n):
    temp2=0
    while len-1-2*n >= 0:
        temp2=temp2+int(num[len-1-2*n])
        n=n+1
    return temp2

result=(secondDigitNums(n)+singleDigitNums(n))

if result % 10 == 0 :
    print("Bu bir kredi karti numarasidir.")
else:
    print("yok")



# 1 2 3 4 5 