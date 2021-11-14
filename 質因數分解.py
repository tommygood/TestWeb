def isPrime(n):
    #定義:n的因數只有1和n,則n為prime
    div = 2
    while div < n :
        if n % div == 0:#可以整除,不是prime
            return False
        div = div + 1 #測下一個數字
    return True #2~n-1 都不能整除,所以是質數

def findSol(n):#n的因數一定會比n小
    x=1 #從1到n找與n相除餘0的數
    y=0 #設y等於n的因數
    while x < n:
        x=x+1
        if n%x == 0 and isPrime(x) == True :
            y = x
    return y
def main():
    n=int(input())
    print(findSol(n))

if __name__ == '__main__':
    main()
            
        
        
        

