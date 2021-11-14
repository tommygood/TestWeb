def check(t):
    loc = []
    custo = 0
    for i in range(len(t)) : #找出next的位置
        if t[i] == 'NEXT' :
            loc = loc + [i]
    for l in loc :
        for i in range(len(t)) :
            if i < l and t[i] != 'NEXT': #比next位置前面就減1
                t[i] = int(t[i]) - 1
    for i in t :
        if i != 'NEXT' and i != 'END' and int(i) > 0 :
            custo = custo + 1 #總共剩幾人
    print(custo)
    
def book(total,infor):
    if  len(infor) == 4 and infor[3].isnumeric() : #客人
        total = total + [int(infor[3])]
        return total
    elif len(infor) == 5 :
        total = total + [int(infor[3]+infor[4])]
        return total
    elif infor == 'END' : #End
        total = total + [infor] #加end
        return total
    else :  #next
        total = total + [infor]
        return total
    
def main():
    hotel = True
    total = []
    while 'END' not in total : #先建立名單
        total = book(total,input())
    print(total)
    check(total)
    print(total)
              
if __name__ == '__main__' :
    main()


        
