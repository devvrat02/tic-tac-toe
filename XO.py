theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def winner():
    if theBoard['top-L']== theBoard['top-M'] and theBoard['top-M']== theBoard['top-R']:
        if theBoard['top-R']=='X' or theBoard['top-R']=='O':
                print("winner is ", theBoard['top-L'])
                return 1
    if theBoard['mid-L']== theBoard['mid-M'] and theBoard['mid-L']== theBoard['mid-R']:
        if theBoard['mid-R']=='X' or theBoard['mid-R']=='O':
            print("winner is ", theBoard['mid-L'])
            return 1        
    if theBoard['low-L']== theBoard['low-M'] and theBoard['low-M']== theBoard['low-R']:
        if theBoard['low-R']=='X' or theBoard['low-R']=='O':
            print("winner is ", theBoard['low-L'])
            return 1
    if theBoard['low-L']== theBoard['mid-M'] and theBoard['mid-M']== theBoard['top-R']:
        if theBoard['top-R']=='X' or theBoard['top-R']=='O':
            print("winner is ", theBoard['top-R'])
            return 1
    if theBoard['low-R']== theBoard['mid-M'] and theBoard['mid-M']== theBoard['top-L']:
        if theBoard['top-L']=='X' or theBoard['top-L']=='O':
            print("winner is ", theBoard['top-L'])
            return 1
    if theBoard['low-R']== theBoard['mid-R'] and theBoard['mid-R']== theBoard['top-R']:
        if theBoard['top-R']=='X' or theBoard['top-R']=='O':
            print("winner is ", theBoard['low-R'])
            return 1
    if theBoard['low-M']== theBoard['mid-M'] and theBoard['mid-M']== theBoard['top-M']:
        if theBoard['top-M']=='X' or theBoard['top-M']=='O':
            print("winner is ", theBoard['low-M'])
            return 1
    if theBoard['low-L']== theBoard['mid-L'] and theBoard['mid-L']== theBoard['top-L']:
        if theBoard['top-L']=='X' or theBoard['top-L']=='O':
            print("winner is ", theBoard['low-L'])
            return 1
    else:
        return 0

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print ('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    if move == 'top-L' or move =='top-M' or move =='top-R' or move == 'mid-L' or move == 'mid-M' or move =='mid-R' or move =='low-L' or move =='low-M' or move == 'low-R':
        if theBoard[move]==' ':
            theBoard[move] = turn
            if turn == 'X':
                turn = 'O' 
            else:
                turn = 'X'
    else:
        loopflag = True
        while loopflag:
            printBoard(theBoard)
            print('Turn for ' + turn + '. Move on which space?')
            move = input()
            if move == 'top-L' or move =='top-M' or move =='top-R' or move == 'mid-L' or move == 'mid-M' or move =='mid-R' or move =='low-L' or move =='low-M' or move == 'low-R':
                if theBoard[move]==' ':
                    theBoard[move] = turn
                    if turn == 'X':
                        turn = 'O'
                    else:
                        turn = 'X'
                loopflag = False
    if winner():
       break
        
          
printBoard(theBoard)
