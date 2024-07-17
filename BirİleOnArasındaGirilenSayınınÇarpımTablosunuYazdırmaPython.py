i=input("Sayıyı giriniz:")
i=int (i)
n=0
while True:
    if i>=1 and i<=10 and n<=10:
        carpim=i*n
        print(carpim)
        n=n+1
    else:
         i=input("Sayıyı giriniz:")
         i=int (i)
