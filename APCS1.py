def main():
    n = int(input())
    total_first = input().split()
    total = turn_int(total_first) # map(x,y) = put the y(parameter) into the x function 
    min_num,max_num = findSol(total,n)
    print(*sorted(total),min_num,max_num)

def turn_int(total) :
    for i in range(len(total)) :
       total[i] = int(total[i])
    return total
    
def findSol(total,n) :
    min_num = 0
    max_num = 100
    for i in range(n) :
        if total[i] < 60 and total[i] > min_num :
            min_num = total[i]
        if total[i] >= 60 and total[i] < max_num :
            max_num = total[i]
    return min_num,max_num
    
if __name__ == "__main__" :
    main()