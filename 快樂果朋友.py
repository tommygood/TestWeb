#money:預算
#target:要買的數量
#kind:水果種類數
#price:每種水果的單價
#got:每種水果已買好的數量
#pos:我要負責買的種類
def findSol(money,target,kind,price):
    mySol(money,target,kind,price,[],0)

def mySol(money,target,kind,price,got,pos):
    if pos == kind:
        if target == 0 :
            print(*got)
        return
    for i in range(min(target,money//price[pos]),-1,-1):   
        mySol(money-i*price[pos],target-i,kind,price,got+[i],pos+1)

def main():
    money,target,kind = map(int,input().split())
    price = list(map(int,input().split()))
    if min(price)*target > money :
        print('無法買滿')
    else :
        findSol(money,target,kind,price)

if __name__ == '__main__' :
    main()
