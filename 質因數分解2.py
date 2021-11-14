#學號:109213059
#姓名:王冠權
def isPrime(n):
    #定義:n的因數只有1和n,則n為prime
    div = 2
    while div < n :
        if n % div == 0:#可以整除,不是prime
            return False
        div = div + 1 #測下一個數字
    return True #2~n-1 都不能整除,所以是質數
            
            
def main():#n的因數一定會比n小
    n=int(input())
    x=2
    while x <= n :#利用迴圈做n的質因數分解
        if n % x == 0 and isPrime(x) == True :#同時滿足為n的因數及為質數            
            print(int(x))
            n = n // x #讓就算n的質因數為同一個也可以繼續輸出
        else:
            x=x+1 #x不為n的因數的時候,就+1直到找到    
if __name__ == '__main__':
    main()
            
        
        
        

