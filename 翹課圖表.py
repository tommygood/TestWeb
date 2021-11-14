
def main():
    number=int(input())#總共要幾個數字
    z=0 #從0開始
    x=0 #從0開始
    y=1 #從1開始
    total=''
    sep=[]
    sep.append(int(input()))#分別要甚麼數字
    maxx=sep[0]
    alt=[]
    alt.append(sep[0])
    z=1
    while z < number :        
        sep.append(int(input()))#分別要甚麼數字
        alt.append(int(sep[z]))
        if alt[z] > maxx  :
            maxx = alt[z]
        z=z+1
    maxxx=maxx+2
    while maxx < maxxx :
        print(str(maxxx),'','.. '*number)
        maxxx=maxxx-1
    while 1 <= maxxx :
        print(str(maxxx),' ',end='')
        for c in range(number):
            if alt[c] < maxxx :
               print('.. ',end='')
            else :
                print('## ',end='')
        print()
        maxxx=maxxx-1
            
    while x <= number:        
        total=total+'0'+str(x)+' '
        x=x+1
 
    print(total)
    

main()



        




