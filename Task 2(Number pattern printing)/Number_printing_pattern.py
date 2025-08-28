print("Welcome to Number Pyramid Printing")
n = int(input("Enter number of lines of pyramid: "))
num = 1

for i in range(1, n+1):
    print(" " * (n-i), end="")
    for j in range(i):
        print(f" {num}", end="")
        num=num+1

    print()    
    
print("Pyramid printed!")


