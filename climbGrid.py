def number(r,c,got,n,end): #橫線放法有幾種組合
    if n == 0 :
        times = 0
        total = []    # total = 用list of list 的方式算出有幾種
        for i in range(c*2):
            if (i % 2) == 0 :
                total.append([got[i],got[i+1]])
        print(total)
        for l in range(r):
                for x,y in total:
                    if x == l or y == l :
                        l =  dif(l,x,y)
                        times = times + 1
                #print(times)
        return 
    for i in range(r-1):
        number(r,c,got+[i,i+1],n-1,end)
def dif(l,x,y):
    if l == x :
        return x
    else:
        return y
def main():
    r,c=list(map(int,input().split())) #r,c=行,列
    end=[]
    end = end + list(map(int,input().split()))
    number(r,c,[],c,end)
if __name__ == '__main__' :
    main()
