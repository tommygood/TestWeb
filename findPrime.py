#學號:109213059
#姓名:王冠權
def div(k): #是不是質數
    a = 1
    b = []
    while a <= k :
        if k % a == 0 : #餘數為0
            b.append(a)
        a = a + 1
    if len(b) == 2 : #因數只有0跟自己
        return True
    else :
        return False
    
def main():
    a = 2
    b = [] #質數集合
    n = int(input())
    while a <= n :  #一個個加
        if div(a) == True :
            b.append(a)
        a = a + 1
    print(*b)

main()





    
