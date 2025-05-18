
squares = []
charX = "X"
charO = "O"
isEnd = False
players = [charX, charO]
firstPlayerTurn = True

for i in range(9):
    squares.append(" ")
def drawBoard():
    print("1  |2  |3  ")
    print(f" {squares[0]} | {squares[1]} | {squares[2]} ")
    print("___|___|___")
    print("4  |5  |6  ")
    print(f" {squares[3]} | {squares[4]} | {squares[5]} ")
    print("___|___|___")
    print("7  |8  |9  ")
    print(f" {squares[6]} | {squares[7]} | {squares[8]} ")
    print("   |   |   ")

def endGame(winner, isDraw):
    global isEnd
    isEnd = True
    drawBoard()
    if isDraw:
        print("\nThe game has ended with a draw, no one won!\n")
        return
    print(f"\nPlayer {winner} has won the game!\n")
    return


def checkWinner(square):
    if square == charX or square == charO:
        endGame(square, False)

def checkBoard():
    for i in range(3):
        if squares[0+(i-1)*3] == squares[1+(i-1)*3] == squares[2+(i-1)*3]:
            checkWinner(squares[(i-1)*3])
            return
        elif squares[(i-1)+0*3] == squares[(i-1)+1*3] == squares[(i-1)+2*3]:
            checkWinner(squares[i-1])
            return
        elif squares[0] == squares[4] == squares[8]:
            checkWinner(squares[4])
            return
        elif squares[2] == squares[4] == squares[6]:
            checkWinner(squares[4])
            return
    occupiedSquares = 0
    for square in squares:
        if square in players:
            occupiedSquares += 1
    if occupiedSquares == 9:
        endGame("draw", True)
            

def playerInput():
    global firstPlayerTurn
    possibleInputs = [1,2,3,4,5,6,7,8,9]
    playerInput = 0
    mark = players[0] if firstPlayerTurn else players[1]
    firstPlayerTurn = not firstPlayerTurn
    while playerInput not in possibleInputs:
        try:
            playerInput = int(input(f"Provide a square you want to mark ({mark}): "))
        except ValueError:
            print("Please enter a valid integer representing free slot\n")
        if squares[playerInput-1] in players:
            playerInput = 0
            print("This slot is alreade taken!\n")
    squares[playerInput-1] = mark

while not isEnd:
    drawBoard()
    playerInput()
    checkBoard()
