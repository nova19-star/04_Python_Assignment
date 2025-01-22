# Write a python program to find Armstrong number in interval	100 - 1000
i = int(input("Enter lower limit: "))
u = int(input("Enter upper limit: "))
print("Armstrong number beetween", i, "and", u)
for i in range(i,u):
    n = i 
    s = 0 
    d = 0
    while(n!=0):
        d=d+1
        n=n//10
    n = i
    while(n!=0):
        s = s+(n%10)**d
        n = n//10
    if(s==i):
        print(i)
