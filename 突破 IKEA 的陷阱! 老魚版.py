def findSol(n,data,beginr,beginc,endr,endc):
    #建立每一個點與原點間的距離,由於起點終點都要算
    #因此合法的距離最小為1,以0代表某點還找不到路徑
    distance=[[0 for i in range(n)]for i in range(n)]
    #checklist存放要處理的點,一開始只有起點
    checkList,distance[beginr][beginc] = [[beginr,beginc]],1
    while len(checkList) != 0 :
        [r,c] = checkList.pop(0) #拿出最前面還沒有處理的點
        if endr == r and endc == c :#抵達終點了
            return distance[r][c]
        #否則處理四個方向的鄰接點
        for [rDif,cDif] in [[1,0],[-1,0],[0,1],[0,-1]]:
            nextr,nextc = r+rDif,c+cDif
            if nextr<0 or nextr >= n or nextc < 0 or nextc >= n : #超越邊界
                continue #跳過此點
            if data[nextr][nextc] == 0 and distance[nextr][nextc] == 0:
                #此點沒有來過
                distance[nextr][nextc] = distance[r][c]+1
                checkList.append([nextr,nextc])
def main():
    data=[]
    n = int(input())
    for i in range(n):
        data.append(list(map(int,input().split())))
    begin = list(map(int,input().split()))
    end = list(map(int,input().split()))
    print(findSol(n,data,begin[0],begin[1],end[0],end[1]))

if __name__ == '__main__' :
    main()



    
