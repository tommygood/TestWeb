def main() : # Magic Square,top left only
    n = int(input()) # n*n,n must be odd
    findSol(n,[[0 for i in range(n)] for i in range(n)]) # put 0

def print_stan(total) : # print standard
    for i in range(len(total)) :
        for j in range(len(total)) :
            print('{:2}'.format(total[i][j]),end = " ") # line up
        print()

def findSol(n,total) :
    a = 0 # row
    b = n//2 # column
    total[a][b] = 1 
    for i in range(2,n*n+1) :
        store_a = a
        store_b = b
        a -= 1
        b -= 1
        if a <= -1 : # out of bounds
            a = n-1
        if b <= -1 :
            b = n-1
        if total[a][b] != 0 : # had number, put under the former number
            a = store_a+1
            b = store_b
        total[a][b] = i
    print_stan(total)
    
if __name__ == "__main__" :
    main()