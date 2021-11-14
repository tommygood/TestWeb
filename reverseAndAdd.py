def main():
    line=int(input())#總共要幾個數字
    order=1 #order=從第一個數字開始算
    while order <= line :
        number = str(input()) #number=要算的數字
        opposite=number[::-1] #opposite=相反的number
        total=int(number) + int(opposite) #total = number + 相反的number
        times=1 #總共算了幾次
        while str(total)[::-1] != str(total): #當number的相反不等於number
            opposite=str(total)[::-1]   #opposite=相反的total
            total=total + int(opposite) #新的total=原本的total+上一行的opposite
            times=times+1               #每次算次數都要加一
        if str(total)[::-1] == str(total): 
            print(times,end=' ')
            print(total)
        order=order+1
    




main()
