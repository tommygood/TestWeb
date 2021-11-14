def findSol(n,m,o,y,x):
    num = [] #相加的數字
    for i in range(m): #把有@的檢查八方
        yn,xn = y[i],x[i]
        number = 0 #要為質數
        for a,b in [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]:
            ys = yn + a 
            xs = xn + b
            if ys >= n : #y大於邊界
                ys = 0
            if ys < 0 :  #y小於邊界
                ys = n-1
            if xs >= n : #x大於邊界
                xs = 0
            if xs < 0 :  #x小於邊界
                xs = n - 1
            if o[ys][xs] == '@' : 
                number = number + 1
        num = num + [number]  #每個#的九宮格的#數量
    for i in num :  #是否為質數
        div = 2
        while div < i :
            if i % div == 0:#可以整除,不是prime
                i = False
            div = div + 1 #測下一個數字
        i = True #2~n-1 都不能整除,所以是質數
    for i in range(m):
        yn,xn = y[i],x[i]
        if num[i] :  #為質數就是可擊掌
            for a,b in [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]:
                ys = yn + a
                xs = xn + b
                if ys >= n : #y大於邊界
                    ys = 0
                if ys < 0 :  #y小於邊界
                    ys = n-1
                if xs >= n : #x大於邊界
                    xs = 0
                if xs < 0 :  #x小於邊界
                    xs = n - 1
                if o[ys][xs] == '@' :
                    o[ys][xs] = '#'
    pos = 0
    for i in range(n):  #有幾個@
        for p in range(n):
            if o[i][p] == '@':
                pos = pos + 1           
    return o,pos
def chart(n,m,y,x): #一開始只有@的地圖
    o = [['X' for i in range(n)] for i in range(n)]
    for i in range(m) :
        o[y[i]][x[i]] = '@'
    return o
def out(n,o,pos): #印出來
    print(pos)
    for i in range(n) :
        row = '' 
        for p in range(n) : 
            row = row + o[i][p] + ' '
        print(row)
def main():
    n = int(input()) # n*n = 場地大小
    m = int(input()) # m = 有幾個位置
    y = []  # y = x 座標
    x = []  # x = y 座標
    for i in range(m):
        a,b = map(int,input().split())
        y,x = y+[a] , x + [b]
    o = chart(n,m,y,x)
    new,pos = findSol(n,m,o,y,x)
    out(n,new,pos)
    
main()


    
        
