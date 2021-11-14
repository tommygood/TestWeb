def number(n):
    total=[]
    low = 0 
    for i in range(n):
        total.append(list(map(int,input().split())))
    begin = list(map(int,input().split()))
    end = list(map(int,input().split()))
    for i in range(2):
        low=low+max(begin[i],end[i])-min(begin[i],end[i])#low = 最少要走幾次
    low = low + 1
    return n,low,total,begin,end
def game(n,br,bc,low,total,er,ec,ans): #br,bc=beginRow,beginColumn. er = endRow
    if br,bc == er,ec :
        return
    for i in range(
def main():
    n,low,total,begin,end=number(int(input()))
    ans=game(n,begin[0],begin[1],low,total,end[0],end[1],0)
    print(ans)
if __name__=='__main__':
    main()
