# 109213059 王冠權
def main() :
    file = open('input_Chinese.txt','r')
    total = [0 for i in range(10)]
    for i in range(10) :
        word = file.readline()
        word = word.split()
        total[i] = int(word[1]) + int(word[2])
    print(findSol(total))
    

def findNum(total) :
    totalNum = [0 for i in range(len(total))]
    

def IntArray(total) :
    for i in range(len(total)) :
        total[i] = int(total[i])
    return total

def findSol(total) :
    ans = [0 for i in range(len(total))]
    for i in range(len(total)) : # seletion sort
        minnum = min(total)
        ans[i] = minnum
        total.remove(minnum)
    print(*ans)

if __name__ == "__main__" :
    main()