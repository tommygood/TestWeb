import random
import sys
w = 6
h = 6
def Board():
    board = []
    for i in range(w): #w = width
        board.append([' ' for i in range(6)])
    return board
def drawBoard(board):
    print('  123456')
    print(' +------+')
    for y in range(h):  #h = height
        print('%s|' % (y+1), end='') #一開始的行數 
        for x in range(w):
            print(board[x][y],end='')#最後的行數
        print('%s|' % (y+1))
    print(' +------+')
    print('  123456')
def onBoard(x,y):
    return True if x >= 0 and x <= w -1 and y >= 0 and y <= h - 1 else False
def check(board,tile,xf,yf): #是否移到正確的位置
    if board[xf][yf] != ' ' or not onBoard(xf,yf):
        return False
    if tile == 'X' :
        oTile = 'O'
    elif tile == 'O':
        oTile = 'X'
    turn = [] #要變的X,O
    for xd , yd in [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]] :
        #每個方向都檢查一次
        x,y = xf , yf  #回到原本的位置
        x = x + xd
        y = y + yd
        while onBoard(x,y) and board[x][y] == oTile :
            # 遇到電腦的棋子
            x = x + xd
            y = y + yd
            if onBoard(x,y) and board[x][y] == tile :
                while True : #反向減回去看哪些要換
                    x = x - xd
                    y = y - yd
                    if x == xf and y == yf : #減完了
                        break
                    turn.append([x,y])
    return False if len(turn) == 0 else turn #沒有要換的代表不行
def validMoves(board,tile):
    move = []
    for x in range(w):
        for y in range(h):
            if check(board,tile,x,y) != False :
                move.append([x,y])
    return move
def newBoard(board,tile):
    copy = Board()
    for x in range(w):
        for y in range(h):
            copy[x][y] = board[x][y]
    for x,y in validMoves(copy,tile):
        copy[x][y] = '.'
    return copy
def score(board):       #算分數
    ts = 0 
    os = 0
    for x in range(w):
        for y in range(h):
            if board[x][y] == 'X' :
                ts = ts + 1
            elif board[x][y] == 'O' :
                os = os + 1
    return ts,os
def tile(): #玩家要X還是O
    tile = ''
    while tile != 'X' and tile != 'O' :
        print(' X or O ')
        tile = input().upper()
    return ['X','O'] if tile == 'X' else ['O','X']
def goFirst(): #誰先
    return 'computer' if random.randint(0,1) == 1 else 'player'
def makeMove(board,tile,xf,yf): #放上棋子
    turn = check(board,tile,xf,yf)
    if turn == False :
        return False
    board[xf][yf] = tile  #一開始的地方
    for x,y in turn:
        board[x][y] = tile  #翻面的地方
    return True  
def isConner(x,y):
    return ( x == 0 or x == w - 1) and (y == 0 or y == h - 1)
def pMove(board,pTile):
    number = [ str(i+1) for i in range(6)]
    while True :
        print('enter your moves , or "quit" to leave , or \
"hints" to get hints')
        move = input().lower()
        if move == 'quit' or move == 'hints' :
            return move
        if len(move) == 2 and move[0] in number and move[1] in number :
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if check(board,pTile,x,y) == False :
                continue
            else :
                break
        else :
            print('enter(1~6)(1~6)')
    return [x,y]
def copyBoard(board):
    boardCopy = Board()
    for x in range(w):
        for y in range(h):
            boardCopy[x][y] = board[x][y]
    return boardCopy
def cMove(board,cTile):
    couldMove = validMoves(board,cTile) #可以下的
    random.shuffle(couldMove)
    bestMove = []
    for x,y in couldMove :
        if isConner(x,y): #可以下角落就先下
            return [x,y]
    best = -1
    for x,y in couldMove :
        copy = copyBoard(board)
        makeMove(copy,cTile,x,y)
        if cTile == 'X' :  #判定是X或O,就加哪個
            scores = score(board)[0]
        elif cTile == 'O' :
            scores = score(board)[1] 
        if max(scores,best) == scores : #要最高分的步
            bestMove = [x,y]
            best = scores
    return bestMove
def printScores(board,pTile,cTile):
    if cTile == 'X' :
        print('you have',score(board)[1],'com have',score(board)[0])
    else :
        print('you have',score(board)[0],'com have',score(board)[1])
def play(pTile,cTile):
    showHints = False
    order = goFirst()
    print(order,'will go first')
    board = Board()
    board[2][2] = 'X'
    board[2][3] = 'O'
    board[3][2] = 'O'
    board[3][3] = 'X'
    while True :
        pValid = validMoves(board,pTile)
        cValid = validMoves(board,cTile)
        if pValid == [] or cValid == [] : #沒有可以動的,結束
            return board
        elif order == 'player' :
            if showHints : #先設為false
                validBoard = newBoard(board,pTile)
                drawBoard(validBoard)
            else :
                drawBoard(board)
            printScores(board,pTile,cTile)
            move = pMove(board,pTile)
            if move == 'quit' :
                print('3q for playing~')
                sys.exit()
            elif move == 'hints' :
                showHints = not showHints # = true
                continue
            else :
                makeMove(board,pTile,move[0],move[1])
            order = 'computer'
        elif order == 'computer' :
            drawBoard(board)
            printScores(board,pTile,cTile)
            input("enter to see com's move")
            move = cMove(board,cTile)
            print(move)
            makeMove(board,cTile,move[0],move[1])
            order = 'player'
def main():
    print('welcome to Reversegame !')
    pTile,cTile = tile()
    while True :
        final = play(pTile,cTile)
        drawBoard(final)
        scores = score(final)
        if pTile == 'X' :
            print('X scored',scores[0],'O scored',scores[1])
            if scores[0] > scores[1] :
                print('you beat com by',scores[0]-scores[1],'points')
            elif scores[1] > scores[0] :
                print('you lost com by',scores[1]-scores[0],'points')
            elif scores[0] == scores[1] :
                print('tie')
        elif pTile == 'O' :
            print('X scored',scores[1],'O scored',scores[0])
            if scores[0] > scores[1] :
                print('com beat you by',scores[0]-scores[1])
            elif scores[1] > scores[0] :
                print('com lost you by',scores[1]-scores[0])
            elif scores[0] == scores[1] :
                print('tie')
        print('do you want to play again')
        if input().lower().startswith('n') :
            break
if __name__ == '__main__' :
    main()
        




    
        









        
 



            





            
    
        





            






                    
            






    
