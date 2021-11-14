def findSol(n,countline,end):
    return myfindSol(n,countline,end,[i for i in range(n)])
#n = 直線
#countline = 橫線
#h = 橫線
#end = 最後的結果
#current = 目前的排法
def myfindSol(v,h,end,current):
    if h == 0 : #沒有橫線了
        if end == current : #找到一組解
            return 1
        return 0
    sol = 0 #找到幾解
    for pos in range(v-1): #任選兩相鄰直線加上橫線
        current[pos],current[pos+1] = current[pos+1],current[pos]
        sol = sol + myfindSol(v,h-1,end,current)
        current[pos],current[pos+1] = current[pos+1],current[pos]
    return sol
def main():
    n,countline = map(int,input().split())
    end = list(map(int,input().split()))
    print(end)

if __name__ == '__main__' :
    main()

