def findSol(n,sort,nowSort,price,got,gotPrice1,gotPrice2,m): #nowSort = 現在可使用的sort
    nowSort = sort[::-1] #got = 上一層的裝飾品
    if len(got) > 0 :  #已經算過的裝飾品要大於0
            for i in range(len(sort)):  #上一層的裝飾品顏色或名字重複,可用的裝飾品減少
                if sort[i][0] == got[::-1][0][0] : 
                    nowSort.remove(sort[i])
                elif sort[i][1] == got[::-1][0][1] :
                    nowSort.remove(sort[i])
    if len(nowSort) == 0 :  #可以用的數字沒了
            return 0
    if m == 0 :  #已經排完聖誕樹了
        if abs(gotPrice1 - gotPrice2) >= n*100: #總奇-總偶 <= n*100
            return 0   
        for i in sort :  #有裝飾品沒有排進聖誕樹就不算
            if i not in got :
                return 0
        return 1
    ans = 0   #ans = 有幾個解
    for i in range(len(nowSort)):
        loc = sort.index(nowSort[i])
        if m % 2 != 0:   #奇數
            gotPrice1 = gotPrice1 + price[loc]
        elif m % 2 == 0:  #偶數
            gotPrice2 = gotPrice2 + price[loc]
        ans = ans + findSol(n,sort,sort[::-1],price,got+[nowSort[i]],gotPrice1,gotPrice2,m-1)
    return ans
def main():
    n = int(input()) #n = 有幾種裝飾品
    sort = list(map(str,input().split())) #sort = 各別是哪一種
    price = list(map(int,input().split())) #price = 各別是多少錢
    m = int(input()) #m = 有幾層聖誕樹
    print(findSol(n,sort,sort[::-1],price,[],0,0,m))
if __name__ == '__main__' :
    main()
