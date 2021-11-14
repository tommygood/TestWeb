def main(): #REPT("0",COUNTIF($B$2:$B$139,O46*10+0))
    total = input().split(" ") # input = B 2 139 O46
    Output(total)
    
def Output(total):
    print("=",end = '')
    for i in range(10) :
        print('REPT("',end = '')
        print(i,end = '')
        print(' ",COUNTIF($',end = '')
        print(total[0],end = '')
        print('$',end = '')
        print(total[1],end = '')
        print(':$',end = '')
        print(total[0],end = '')
        print('$',end = '')
        print(total[2],end = '')
        print(',',end = '')
        print(total[3],end = '')
        print('*10+',end = '')
        print(i,end = '')
        if i != 9 :
            print('))&',end ='')
        else :
            print('))',end ='')


if __name__ == "__main__" :
    main()
