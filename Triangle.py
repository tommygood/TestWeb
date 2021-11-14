#學號:109213059
#姓名:王冠權
def main():
    #輸入a b c
    a=int(input())
    b=int(input())
    c=int(input())
    #讓abc由小到大排列
    if a > b :
        a,b=b,a
    if a > c:
        a,c=c,a
    if b > c:
        b,c=c,b
    #排列出三角形的條件
    if a+b>c and a*a+b*b<c*c:
        print(a,b,c)
        print('Obtuse')
    if a+b>c and a*a+b*b==c*c:
        print(a,b,c)
        print('Right')
    if a+b>c and a*a+b*b>c*c:
        print(a,b,c)
        print('Acute')
    if a+b<=c:
        print(a,b,c)
        print('No')
        

if __name__ == '__main__':
    main()
 

