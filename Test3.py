def main():
    findSol(1,int(input())+1)

def findSol(pos,n):
    if (pos < n):
        print(*["*" for i in range(pos)])
        findSol(pos+1,n)
    return

main()