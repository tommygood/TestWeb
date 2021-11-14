def genOddMagic(n):
    data=[[0 for c in range(n)]for r in range(n)] #先用0填滿
    r,c=0,n//2 #最上方正中央,前一個填的位置
    data[r][c] = 1
    for num in range(2,n*n+1): #依序填入數字2~n*n
        nextR,nextC=r-1,c+1 #原位置右上
        if nextR < 0 : #超過上邊界
            nextR=n-1  #移到最下面
        if nextC >= n : #超過右邊界
            nextC=0     #移到最左邊
        if data[nextR][nextC] != 0 : #已經填過了
            nextR,nextC=r+1,c       #原位置下面
        data[nextR][nextC] = num #把數字填進去
        r,c = nextR,nextC     #移動位置
    return data
def printByRow(data):
    for r in data :
        for v in r :
            print(str(v).rjust(2,' '),end=' ')
        print()
    return data
def number(n,board):
    r,c,allow=n//2,n//2,[[True for j in range(n)]for i in range(n)]
    rDif,cDif=[0,-1,0,1],[-1,0,1,0]
    print(board[r][c],end=' ')
    allow[r][c] = False
    for num in range(2,n*n+1):
        if allow[r+rDif[d]][c+cDif[d]] :
            r,c,d=r+rDif[d],c+cDif[d],(d+1)%4
        else :
            r,c=r+rDif[(d-1)%4],c+cDif[(d-1)%4]
        print(board[r][c],end=' ')
        allow[r][c] = False    
    
def main():
    n=int(input())
    board=genOddMagic(n)
    number(n,board)
    printByRow(board)
    
main()
