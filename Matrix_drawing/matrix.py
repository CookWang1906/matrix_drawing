#info: In this repository you will learn about matrix and stuff
import numpy as np
def pick(): 
    print("A - Math with matrix")
    print("B - Draw matrix")
    pick = input("Please choose: ")
    
    if pick == "A":
        math_matrix()
    elif pick == "B":
        draw_matrix()
    else:
        print("Please choose again!\n")

#basic math in matrix    
def math_matrix():
    A = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
    
    B = np.array([[3,2,1],
                  [6,5,4],
                  [9,8,7]])
    print(A+B)
    print(A-B)
    print(A@B) #Multiply: AB = BA (why 42 = 1x3+2x6+3x9); row1 x column1,2,3 = 3 first number in the answer then we move down to the next row and follow with the pattern
    print("---------------------------\n")
    return pick()

#how to matrix
def draw_matrix():
    Row = int(input("\nEnter the number of rows: "))
    Column = int(input("Enter the number of columns: "))
# Initialize matrix
    matrix = [] #make an empty matrix
    print("Enter the entries row wise: ")
# A for loop for row entries
    for row in range(Row):
        a = [] #empty list
    # A for loop for column entries
        for column in range(Column):   
            a.append(int(input())) #add number to list
        matrix.append(a) #add list to matrix
# For printing the matrix
    for row in range(Row):
        for column in range(Column):
            print(matrix[row][column], end=" ")
        print()
    return draw_matrix()
pick()