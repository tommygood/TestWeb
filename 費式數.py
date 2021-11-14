#費式數
#f(n) = f(n-1)+f(n-2)
#1 1 2 3 5 8
def f(n):
    if n <= 1 :
        return n
    n_1,n_2=1,0 #n_1代表f(n-1)的值,n_2代表f(n-2)的值
    num = 1 #要計算第幾個費式數
    while num < n :
        n_2,n_1 = n_1, n_1+n_2
        num = num + 1
    return n_1

if __name__ == '__main__' :
    print(f(int(input())))
