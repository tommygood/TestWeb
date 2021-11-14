# 109213059 王冠權
def main() :
    file = open('input.txt','r')
    total = file.readline()
    file.close()
    total = total.split()
    print("王冠權 109213059 請輸入檔案名稱，請輸入你的input.txt")
    findSol(IntArray(total))

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