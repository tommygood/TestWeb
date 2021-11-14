import random
def drawboard(board):
    print(board[0]+'|'+board[1]+'|'+board[2]+'|'+board[3]+'|'+board[4]+'|'+board[5]+'|'+board[6]+'|')
    print('-+-+-+-+-+-+-+')
    print(board[7]+'|'+board[8]+'|'+board[9]+'|'+board[10]+'|'+board[11]+'|'+board[12]+'|'+board[13]+'|')
    print('-+-+-+-+-+-+-+')
    print(board[14]+'|'+board[15]+'|'+board[16]+'|'+board[17]+'|'+board[18]+'|'+board[19]+'|'+board[20]+'|')
    print('-+-+-+-+-+-+-+')
    print(board[21]+'|'+board[22]+'|'+board[23]+'|'+board[24]+'|'+board[25]+'|'+board[26]+'|'+board[27]+'|')
    print('-+-+-+-+-+-+-+')
    print(board[28]+'|'+board[29]+'|'+board[30]+'|'+board[31]+'|'+board[32]+'|'+board[33]+'|'+board[34]+'|')
    print('-+-+-+-+-+-+-+')
    print(board[35]+'|'+board[36]+'|'+board[37]+'|'+board[38]+'|'+board[39]+'|'+board[40]+'|'+board[41]+'|')
def playerColor():
    print('which color do you want ? r(red) or b(blue)')
    color = input()
    if color == 'r' :
        return 'r','b'
    else:
        return 'b','r'
def goFirst():
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'
def makeMove(board,color,move):
    board[int(move)] = color
    
def isWinner(b,c):
    return(b[0] == c and b[1] == c and b[2] == c and b[3] == c ) 

def playerMove(board):
    print('where do you want to pick?(0~41)')
    move =input()
    return move
def main():
    board=[' 'for i in range(42)]
    order = goFirst()
    player,com=playerColor()
    while isWinner(board,player) != True :
        move=playerMove(board)
        makeMove(board,player,move)
        drawboard(board)

if __name__ == '__main__' :
    main()

   
        
 
