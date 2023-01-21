''' This class contains functions that implement the basic functions to start the game '''

# Import the parent class and thier functions
from board import Board

# Import the time module to get the date and time for the name of the text file
from datetime import datetime

# Start of the 'Game' class
class Game(Board):
    
    # Class constructor 
    def __init__(self):

        ''' The constructor of the 'Game' class takes in the names of the players 
            and performs a validation check.
            Only if the names entered are valid, the players can proceed forward
            Otherwise, they are asking to re-enter the names  '''

        # Calling the constructor of the parent class
        super().__init__()  

        # Validation check for the name of 'player 1'
        while True:
            self.player1 = input("Enter the name of Player 1: ")
            if(self.player1 and self.player1.strip()):  # Checking in the input is not empty by removing the whitespaces
                break
            else:
                print("Invalid entry for Player 1's name, Please input a valid name!")  # Ask the user to re-enter
                continue
        
        # Validation check for the name of 'player 2'
        while True:
            self.player2 = input("Enter the name of Player 2: ")
            if(self.player2 and self.player2.strip()):  # Checking in the input is not empty by removing the whitespaces
                break
            else:
                print("Invalid entry for Player 2's name, Please input a valid name!")
                continue

    #-------------------------------------------------End of constructor------------------------------------------------#
    
    def startGame(self):

        ''' It asks if the user wants to start the game 
            If yes -> start game play
            If no -> print message and exit
            If invalid -> ask the user again 

            Calculate the time and date using the datetime() function to create the file name 
            Renders the initial board
            Calls the play game function  '''

        while True:
            self.gameStart = input("Begin Game Play? (Y/N): ")
            if(self.gameStart.casefold() == 'y'):   # If user wants to start the game

                # Using the datetime function() - get the year, month, day, hour, minute, second to create the file name
                now = datetime.now()
                year = str(now.year)
                month = str(now.month)
                day = str(now.day)
                hour = str(now.hour)
                minute = str(now.minute)
                second = str(now.second)

                # Get the file name by appending the above created strings
                self.fileName = self.player1 + "_" + self.player2 + "_" + month + "_" + day + "_" + year + "_" + hour + "." + minute +"." + second + '.txt'

                # Open the file and write the start message 
                with open(self.fileName,'w') as f:
                    print("Checkers game start", file=f)

                # Render the initial board on the console and the file
                self.displayBoard(self.fileName, "", "", "", "")    #Pass empty parameters in the beginning

                # Call function to start playing the game 
                self.playGame()
                break

            elif(self.gameStart.casefold() == 'n'): # If user does not want to start the game
                print("Thank you for using Checkers game!")
                break

            else:
                print("Invalid entry!") # If user enters invalid input

    #-------------------------------------------------End of function------------------------------------------------#

    def player1_MoveType(self):

        ''' This function determines what move type player 1 wishes to do
            Depending on the move type, it calls the modify board function in the parent class  '''

        print(f"Enter {self.player1} move type. ")  

        print("1. Make a single move/jump")
        print("2. Make a double jump")

        userMoveChoice = input("=> ")   # Get the choice from the user 

        if(userMoveChoice == '1'):  # If user wishes to do a single move/jump
            self.player1_Moves()    # Call the player move function

        elif(userMoveChoice == '2'):    # If user wishes to do a double jump
            print("Enter the first jump (start, jump location 1): ")    # Get the first jump details
            self.player1_start, self.player1_jump1 = input((f"{self.player1} move: ").lower()).split(',')
            # Function call to modify the board with the moves
            self.modifyBoardPlayer1(self.player1,self.player1_start, self.player1_jump1)

            # Start a loop to check if the second move is valid or not 
            while True:
                print("Enter the second jump (jump location 1, jump location 2): ") # Get the second jump details

                self.player1_jump2, self.player1_end = input((f"{self.player1} move: ").lower()).split(',')

                # Check if the end of the first jump is the start location of the second jump - (i.e) jumping the same piece
                if(self.player1_jump1 == self.player1_jump2):   
                    # Function call to modify the board with the moves
                    self.modifyBoardPlayer1(self.player1,self.player1_jump2, self.player1_end)
                    break
                    
                else:
                    print("Jump entered is invalid!")   # If jump is invalid - ask the user again
            
            #--------------------------------------------End of loop---------------------------------------------#
                    
        else:   # If the user enters wrong move choice - call the function again
            print("Wrong choice! Please try again!")
            self.player1_MoveType()
    
    #-------------------------------------------------End of function------------------------------------------------#

    def player1_Moves(self):

        ''' This function simply takes the move information from the player1 and calls the modify board function '''
        self.player1_start, self.player1_end = input((f"{self.player1} move: ").lower()).split(',')
        self.modifyBoardPlayer1(self.player1,self.player1_start, self.player1_end)  # Function call

    #-------------------------------------------------End of function------------------------------------------------#

    def player2_MoveType(self):

        ''' This function determines what move type player 1 wishes to do
            Depending on the move type, it calls the modify board function in the parent class  '''

        print(f"Enter {self.player2} move type. ")  

        print("1. Make a single move/jump")
        print("2. Make a double jump")

        userMoveChoice = input("=> ")   # Get the choice from the user 

        if(userMoveChoice == '1'):  # If user wishes to do a single move/jump
            self.player2_Moves()    # Call the player move function

        elif(userMoveChoice == '2'):    # If user wishes to do a double jump
            print("Enter the first jump (start, jump location 1): ")    # Get the first jump details

            self.player2_start, self.player2_jump1 = input((f"{self.player2} move: ").lower()).split(',')
            # Function call to modify the board with the moves
            self.modifyBoardPlayer2(self.player2,self.player2_start, self.player2_jump1)

            # Start a loop to check if the second move is valid or not 
            while True:
                print("Enter the second jump (jump location 1, jump location 2): ") # Get the second jump details

                self.player2_jump2, self.player2_end = input((f"{self.player2} move: ").lower()).split(',')
                # Check if the end of the first jump is the start location of the second jump - (i.e) jumping the same piece
                if(self.player2_jump1 == self.player2_jump2):   #To check if the same piece is being jumped
                    # Function call to modify the board with the moves
                    self.modifyBoardPlayer2(self.player2,self.player2_jump2, self.player2_end)
                    break
                    
                else:
                    print("Jump entered is invalid!")   # If jump is invalid - ask the user again

            #--------------------------------------------End of loop---------------------------------------------#
                    
        else:   # If the user enters wrong move choice - call the function again
            print("Wrong choice! Please try again!")
            self.player2_MoveType()
    
    #-------------------------------------------------End of function------------------------------------------------#
        
    def player2_Moves(self):

        ''' This function simply takes the move information from the player1 and calls the modify board function '''
        self.player2_start, self.player2_end = input((f"{self.player2} move: ").lower()).split(',')
        self.modifyBoardPlayer2(self.player2,self.player2_start, self.player2_end)  # Function call
    
    #-------------------------------------------------End of function------------------------------------------------#

    def checkEndGame(self): 

        ''' This function checks if either player has any pieces left on the board   '''

        if(self.count_player1Pieces == 0 or self.count_player2Pieces == 0):
            return True     # The game has ended as one of the player does not have any pieces left on the board
        else:
            return False    # Game has not ended

    #---------------------------------------End of function-----------------------------------------#

    def playGame(self):
        
        ''' This function is the main driver that alternates between the two players 
            After each input, it checks if the game is ended or not 
            It calls two different functions, depending on which player is playing   '''

        print("Please enter in the format 'start point' , 'end point'. (E.g): c-2,d-3") # General desciption of how the input should be entered

        # Loop runs untill the game is over 
        while True: 
            # Check if the game has not ended 
            isEndGame = self.checkEndGame()

            if(isEndGame):  # If game has ended - break out of the loop 
                break   
            else:
                self.player1_MoveType() # Call the function for player 1
                isEndGame = self.checkEndGame() # Check if game has ended after player 1 moves 

                if(isEndGame):  # If game has ended - break out of the loop 
                    break
                else:
                    self.player2_MoveType() # Call the function for player 2

        #------------------------------------End of loop---------------------------------------------#
            
        # Check who is the winner by calculating which player has no pieces on the board
        if(self.count_player1Pieces == 0):
            self.printWinner(self.player2)  # Call the print function
        else:
            self.printWinner(self.player1)  # Call the print function
            
        # Print exit message
        print("Thank you for using Checkers game!")

    #----------------------------------------End of function-----------------------------------------#
            
    def printWinner(self,winnerName):

        ''' This function simply prints the winner of the game - to the console and
            writes to the file  '''
        
        print(f"Winner is {winnerName} !")
        with open(self.fileName,'a') as f:
            print(f"Winner is {winnerName} !", file = f)
    
    #---------------------------------------End of function-----------------------------------------#

#-------------------------------------------------End of class------------------------------------------------#
            

    
