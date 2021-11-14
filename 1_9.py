def magicExp(data):
    return (data[0]*10+data[1])*data[2]==(data[3]*10+data[4]) and \
           ((data[3]*10+data[4])+(data[5]*10+data[6]))==(data[7]*10+data[8])
def findSol():
    myPerm([i for i in range(1,10)], [] ,9,magicExp)

def myPerm(data,got,n,valid):
    if n == 0 :   #如果都選完了
        if vaild(data):
            print(*got) #印出來
        return
    for pos in range(len(data)):  #任選data中的一個元素
        # 再請同學選剩下的n-1個元素
        myPerm(data[0:pos]+data[pos+1:],got+[data[pos]],n-1,valid)


def main():
    findSol()
main()
