#triangle or also known as the pyramid
def pick():
    print("\nA - Triangle of numbers")
    print("B - Reversed triangle full of *") #take this as an example and learn how to make reversed triangle full of numbers yourself.
    print("C - Pascal's triangle")
    choices = input("Please pick one to continue: ")
    
    if choices == "A":
        pyramid()
    elif choices == "B":
        reversed_pyramid()
    elif choices == "C":
        pascal()
    else:
        print("Choose again lil buddy.")
        return pick()
    
#Full pyramid of numbers
def pyramid():
    rows = int(input("Enter number of rows: "))

    k = 0
    count=0
    count1=0

    for i in range(1, rows+1):
        for space in range(1, (rows-i)+1):
            print("  ", end="")
            count+=1
    
        while k!=((2*i)-1):
            if count<=rows-1:
                print(i+k, end=" ")
                count+=1
            else:
                count1+=1
                print(i+k-(2*count1), end=" ")
            k += 1
    
        count1 = count = k = 0
        print()
    return pick()

#Reversed pyramid of *
def reversed_pyramid():
    rows = int(input("Enter number of rows: "))

    for i in range(rows, 1, -1):
        for space in range(0, rows-i):
            print("  ", end="")
        for j in range(i, 2*i-1):
            print("* ", end="")
        for j in range(1, i-1):
            print("* ", end="")
        print()
    return pick()
    
#Pascal's Triangle
def pascal():
    rows = int(input("Enter number of rows: "))
    coef = 1    

    for i in range(1, rows+1):
        for space in range(1, rows-i+1):
            print(" ",end="")
        for j in range(0, i):
            if j==0 or i==0:
                coef = 1
            else:
                coef = coef * (i - j)//j
            print(coef, end = " ")
        print()
    return pick()
pick()