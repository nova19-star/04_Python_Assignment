# Write a python program to find the factor of a number without using function 

n = int(input("Enter a number:"))
print("Factors = ",end='')
for i in range(1, n+1):
    if(n%i==0):
        print(i,end='')
      
