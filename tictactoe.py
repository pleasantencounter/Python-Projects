#!/usr/bin/python
count = 0
player = 'X'
score = False
dictBoard = {'1':' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }
boardList= []
xSet = set()
oSet = set()
newDict = {}

def displayBoard(board):
    print(board['1'],board['2'],board['3'],sep="|")
    print('-+-+-')
    print(board['4'],board['5'],board['6'],sep="|")
    print('-+-+-')
    print(board['7'],board['8'],board['9'],sep="|")

def changeplayer():
    global player
    global count
    if  player == 'X':
        player ='O'
    else:
        player ='X'
    count +=1

def checkScore(board):
    global newDict
    for key,value in board.items():
        if board[key] != " ":
            newDict={value:key}
        
        for user, position in newDict.items():
            if user == 'X':
                xSet.add(position)
                scoreLogic(xSet)
            elif user == 'O':
                oSet.add(position)
                scoreLogic(oSet)

    print(f"X: {xSet}")         
    print(f"O: {oSet}")
   

def resetGame(var, board):
    global score
    global xSet
    global oSet
    global count

    var.lower()
    if var == 'y':
        #clears board
        for key in board:
            board[key] = ' '
        #prints board then resets board variables
        displayBoard(dictBoard)
        score = False
        xSet = set()
        oSet = set()
        count = 0
    else:
        exit()

       
def scoreLogic(playerSet):
    global score
    if all(num in playerSet for num in ['1','2','3']):
        score = True
        return score
    elif all(num in playerSet for num in ['4','5','6']): 
        score = True
        return score
    elif all(num in playerSet for num in ['7','8','9']):
        score = True
        return score
    elif all(num in playerSet for num in ['1','4','7']):
        score = True
        return score
    elif all(num in playerSet for num in ['2','5','8']):
        score = True
        return score
    elif all(num in playerSet for num in ['3','6','9']):
        score = True
        return score
    elif all(num in playerSet for num in ['1','5','9']):
        score = True
        return score
    elif all(num in playerSet for num in ['3','5','7']):
        score = True
        return score
    else:
        score = False
        return score

def mainGame ():
    while count < 9:
        position = input("Player enter position: ")
        if dictBoard[position] == ' ':
            dictBoard[position]=player
            displayBoard(dictBoard)
            checkScore(dictBoard)
            
        else:
            print("Choose a different position")
            continue
        
        print(score)
        if score == True:
            print("Winner Winner Chicken Dinner!")
            resume = str(input("You would you like to continue, press Y: "))
            resetGame(resume,dictBoard)
            print(score)

        changeplayer()

if __name__ == "__main__":
    mainGame()
