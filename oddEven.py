#學號:109213059
#姓名:王冠權
def main():
    number = input() #輸入的數字
    odd=0 #odd=奇數
    even=1 #even=偶數
    oddtotal=0 #oddtotal=奇數和
    eventotal=0 #eventotal=偶數和
    total=len(number) #total=總共有幾個數字
    
        
    while odd < total :
        odd1=int(number[odd]) 
        oddtotal=oddtotal+odd1 #奇數一直相加
        odd = odd + 2
        
    while even < total :
        even1=int(number[even])
        eventotal=eventotal+even1 #偶數一直相加
        even = even + 2

    print('odd :',oddtotal)
    print('even :',eventotal)
        
        

if __name__ == '__main__':
    main()
