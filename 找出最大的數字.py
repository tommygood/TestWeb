def main():
    n=int(input())#一共要處理幾個數字
    x=0#目前的最大值,一開始要設最小
    y=0#已經處理幾個數字了
    while y<n:
        z=int(input())
        if z>x :
            x=z
        y=y+1
    print(x)

if __name__ =='__main__':
    main()
        
    
