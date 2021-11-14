def main():
    #輸入三個數字
    a=int(input())
    b=int(input())
    c=int(input())
    #讓a<=b<=c
    if a > b :
        a,b=b,a
    if a > c:
        a,c=c,a
    if b > c:
        b,c=c,b
    print(a,b,c)
if __name__ == '__main__':
    main()

