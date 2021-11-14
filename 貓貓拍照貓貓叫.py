def perm(cats,result,doNotTogether,n):
    #中止條件
    if n == 0 :
        print(*result)
        return
    for i in range(len(cats)) :
        if len(result) == 0 or (result[-1] not in doNotTogether \
        or cats[i] not in doNotTogether):
            perm(cats[:i]+cats[i+1:],result+[cats[i]],doNotTogether,n-1)

def main():
    #整數 n 表示老俞今天想拍的貓咪數量
    #整數 m 表示有幾隻貓今天不能排在一起
    n,m=map(int,input().split())
    # m 隻貓的名字
    doNotTogether = list(input().split())
    #所有貓的list
    cats= ['鯊魚','hero','mia','黑貓','miu','mogan','mori','mellow','小貓']
    perm(cats,[],doNotTogether,n)

if __name__ == '__main__' :
    main()

        
