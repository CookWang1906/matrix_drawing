#normal numbers squared triangle, reversed numbers squared triangle, FLoyd's triangle
def pick():
    print("\nA - Numbers squared triangle")
    print("B - Inverted numbers squared triangle")
    print("C - Floyd's triangle")
    choices = input("Please pick one to continue: ")
    
    if choices == "A":
        triangle()
    elif choices == "B":
        reverse()
    elif choices == "C":
        floyd()
    else:
        print("Pick again lil homie.")
        return pick()
    
#Draw a triangle with numbers
def triangle():
    rows = int(input("\nEnter number of rows: "))

    for i in range(rows):
        for j in range(i+1):
            print(j+1, end = " ")
        print("")
    return pick()
    
#Reversed numbers triangle
def reverse():
    rows = int(input("Enter number of rows: "))

    for i in range(rows, 0, -1):
        for j in range(1, i+1):
            print(j, end=" ")
        print("")
    return pick()

#Floyd's Triangle
def floyd():
    rows = int(input("\nEnter number of rows: "))
    number = 1

    for i in range(1, rows+1):
        for j in range(1, i+1):
            print(number, end=" ")
            number += 1
        print() 
    return pick()
pick()