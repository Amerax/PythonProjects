"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import copy

class TTTBoard:
    def __init__(self, dimensions, trials) -> None:
        self.trials = trials

        self.turn = random.randrange(0,2)
        if self.turn == 1:
            self.botXO = 0
            self.playerXO = 1
        else:
            self.botXO = 1
            self.playerXO = 0
        # 0 = O, 1 = X

        #creates board
        self.dim = dimensions
        self.board = [["_" for _ in range(self.dim)] for _ in range(self.dim)]

    def genBoard(self):
        #generates/resets board
        self.board = [["_" for _ in range(self.dim)] for _ in range(self.dim)]
    
    def displayBoard(self):
        for row in self.board:
            print(" | ".join(row))

    def humanMove(self):
        repeating = True
        while repeating: 
            Xcord = int(input("X value of cell? ")) - 1
            Ycord = int(input("Y value of cell? ")) - 1
            try:
                if self.board[Xcord][Ycord] == "_":
                    repeating = False
                    if self.playerXO == 0:
                        self.board[Xcord][Ycord] = "O"
                    else: 
                        self.board[Xcord][Ycord] = "X"
                else:
                    print('Cord is already taken, choose another. ')
            except:
                print("Your numbers are out of range.")

        self.displayBoard()
        self.turn = 0

    def getBestMove(self):
        cordScores = {}

        for index, row in enumerate(self.board):
            for idx, cell in enumerate(row):
                if cell == "_":
                    cordScores[(index, idx)] = 0
        
        def trial():
            testBoard = copy.deepcopy(self.board)
            availableCords = []
            botMove = True

            for cords in cordScores.keys():
                availableCords.append(cords)

            permAvailableChords = tuple(copy.deepcopy(availableCords))
            
            while self.checkIfWin(testBoard) not in [0, 1, 2]:
                if botMove:
                    seletedChord = random.choice(availableCords) #this is a tuple (X,Y)
                    availableCords.remove(seletedChord)

                    if self.botXO == 0:
                        testBoard[seletedChord[0]][seletedChord[1]] = "O"
                    else:
                        testBoard[seletedChord[0]][seletedChord[1]] = "X"

                    botMove = False
                
                else:
                    seletedChord = random.choice(availableCords) #this is a tuple (X,Y)
                    availableCords.remove(seletedChord)
                    
                    if self.playerXO == 0:
                        testBoard[seletedChord[0]][seletedChord[1]] = "O"
                    else:
                        testBoard[seletedChord[0]][seletedChord[1]] = "X"

                    botMove = True

            if self.checkIfWin(testBoard) == 2:
                return None

            elif self.checkIfWin(testBoard) == 1: #person X won
                    if self.botXO == 0: #bot lost as O
                        for chosenChord in permAvailableChords:
                            xChord = chosenChord[0]
                            yChord = chosenChord[1]

                            if testBoard[xChord][yChord] == "X":
                                cordScores[(xChord, yChord)] += 2

                            elif testBoard[xChord][yChord] == "O":
                                cordScores[(xChord, yChord)] -= 1
                       
                    elif self.botXO == 1: #bot won as x
                        for chosenChord in permAvailableChords:
                            xChord = chosenChord[0]
                            yChord = chosenChord[1]

                            if testBoard[xChord][yChord] == "X":
                                cordScores[(xChord, yChord)] += 2

                            elif testBoard[xChord][yChord] == "O":
                                cordScores[(xChord, yChord)] -= 1

            elif self.checkIfWin(testBoard) == 0: #person 0 won
                    if self.botXO == 0: #bot won as O
                        for chosenChord in permAvailableChords:
                            xChord = chosenChord[0]
                            yChord = chosenChord[1]

                            if testBoard[xChord][yChord] == "X":
                                cordScores[(xChord, yChord)] -= 1

                            elif testBoard[xChord][yChord] == "O":
                                cordScores[(xChord, yChord)] += 2
                       
                    elif self.botXO == 1: #bot lost as x
                        for chosenChord in permAvailableChords:
                            xChord = chosenChord[0]
                            yChord = chosenChord[1]

                            if testBoard[xChord][yChord] == "X":
                                cordScores[(xChord, yChord)] -= 1

                            elif testBoard[xChord][yChord] == "O":
                                cordScores[(xChord, yChord)] += 2

        for _ in range(self.trials): #conducts trials
            trial()
        
        highestScore = 0
        for score in cordScores.values(): #finds highest score
            if score >= highestScore:
                highestScore = score

        for cord, score in cordScores.items(): #returns highest scoring cord
            if score == highestScore:
                return cord

    def botMove(self):
        bestCord = self.getBestMove()
        if self.botXO == 0:
            self.board[bestCord[0]][bestCord[1]] = "O"
        elif self.botXO == 1:
             self.board[bestCord[0]][bestCord[1]] = "X"

        self.displayBoard()
        self.turn = 1

    def checkIfWin(self, board):
        #checks horizontal rows
        for row in board:
            if row == ["X", "X", "X"]:
                return 1 #returning 1 is returning X winning and vice versa
            if row == ["O", "O", "O"]:
                return 0
            
        #checks right to left diagonal
        def check3InRow(lst):
            for i in range(len(lst) - 2):
                if lst[i] == lst[i+1] == lst[i+2]:
                    if lst[i] == "X":
                        return 1
                    elif lst[i] == "O":
                        return 0 


        listOfVals = []
        for index, row in enumerate(board):
            listOfVals.append(row[index])

        if check3InRow(listOfVals) == 1:
            return 1
        elif check3InRow(listOfVals) == 0:
            return 0 
        
        #checks left to right diagonal
        listOfVals.clear()
        for index, row in enumerate(board):
            listOfVals.append(row[self.dim - 1- index])

        if check3InRow(listOfVals) == 1:
            return 1
        elif check3InRow(listOfVals) == 0:
            return 0 

        #checks for tie if all of the board is filled 
        tracker = 0
        for row in board:
            if "_"  in row:
                return None #not a tie yet
            else:
                tracker += 1

            if tracker == self.dim:
                return 2 #tracker keeps track of how many rows without "_"
                
        return None

def play():
    dimensions = 0
    while dimensions <3:
        #takes value for the amount of sqaures on board
        dimensions = int(input("How many squares each length and width? (One value) ")) 
        if dimensions <3:
            print('Minimum value is 3!')

    game = TTTBoard(dimensions, 1500)
    game.genBoard()
    game.displayBoard()

    if game.turn == 0:
        print("The bot is going first")
    else: 
        print("You are going first")
    
    while game.checkIfWin(game.board) not in [0, 1, 2]:
        if game.turn == 0:
            print("It's the robot's turn")
            game.botMove()
        else:
            print("It's your turn")
            game.humanMove()

    if game.checkIfWin(game.board) == 0:
        print('O wins!')
    elif game.checkIfWin(game.board) == 1:
        print('X wins!')
    elif game.checkIfWin(game.board) == 2:
        print("It was a tie!")

play()
