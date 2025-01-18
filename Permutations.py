#logic is print all the even numbers and then the odd numbers if possible excpet when n==2 and n==3
n=int(input())
if n==2 or n==3:
    print("NO SOLUTION")
else:
    for i in range(2,n+1,2):
        print(i,end=" ")
    
    for i in range(1,n+1,2):
        print(i,end=" ")    
        

    
    
    