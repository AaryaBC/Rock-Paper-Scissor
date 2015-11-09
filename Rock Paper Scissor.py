import random

name = input("Enter your name: ")
print("\nHey, " + name + "! Welcome to Rock Paper Scissor \n")
n = int(input("Enter the maximum number of points to win the game: "))
def RPS(my_point, comp_point):
    
    
    if ( my_point < n ) and ( comp_point < n ) :
        x=input("\n\nEnter your choice \n 1. Rock \n 2. Paper \n 3. Scissor \n\n")
        a = x.lower()
        b=["rock","paper","scissor"]
        c=random.choice(b)
        if a == c:
            print("It's a draw")
        elif ( (a == "rock") and (c == "scissor") ) or ( (a == "paper") and (c == "rock") ) or ( (a == "scissor") and (c == "paper") ):
            print("You win because you chose", a, "and the computer chose", c)
            my_point = my_point + 1
            print("Your point is :", my_point)
        elif ( (c == "rock") and (a == "scissor") ) or ( (c == "paper") and (a == "rock") ) or ( (c == "scissor") and (a == "paper") ):
            print("Computer wins because you chose", a, "and the computer chose", c)
            comp_point = comp_point + 1
            print("Computers point is :", comp_point)
        else:
            print("Enter a Valid Choice")
        RPS(my_point, comp_point)
        
        
        
    elif comp_point == n:
        print("The comptuer won because it reached ",n," points")
    elif my_point == n:
        print("You won because you reached ",n," points")
    
    

RPS(0,0)


