import os; os.system("cls")  
n=int(input("Enter number of rows : "))
b=bool(int(input("""Enter 0 for pattern in increasing order and 
any number for pattern in decreasing order : """)))

def star(n,b):
    if b==False:
        x=1
        while x<=n:
                print(x*"*")
                x+=1
    else:
        while n>0:
            print(n*"*")
            n-=1


star(n,b)



























































