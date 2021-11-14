# 排列問題
# 給一個list,請列出其中n個元素的所有排列
def perm(data,n):  #由data任取n個的排列
    myPer(data,[],n)
#data是可選的元素
#got是別人幫忙選好的元素
#n是我負責要選的個數
def myComb(data,got,n):
    if n == 0 : #如果都選完了
        print(*got) #印出來
        return
def myPer(data,got,n):
    if n == 0 :   #如果都選完了
        print(*got) #印出來
        return
    for i in range(len(data)):  #任選data中的一個元素
        # 再請同學選剩下的n-1個元素
        myPer(data[0:i]+data[i+1:],got+[data[i]],n-1)
def main():
    perm('ABCDE',3)

main()
