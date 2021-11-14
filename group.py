# 109213059 王冠權
# https://hackmd.io/H2i1Sq_XTJ24TC0SQrkBxw?view
def main() :
    total = input().split()
    findSol(total,[i for i in range(len(total))])
    
def exist(total) : # 照順序找出還沒找過的人
    for i in range(len(total)) :
        if total[i] != "-1" :
            return i
    return -1

def findSol(total,num) :
    times = 0 # 幾個小團體
    i = 0
    a = True
    while i != -1 : # 當還有人還沒被找過
        j = i # 從頭開始找
        output = [num[i]] # 先把要找的第一個人放進去
        while True :           
            if int(total[j]) == num[i] :
                total[j] = "-1" # 算過變-1
                break
            output.append(total[j])
            store = total[j] # 先存起來
            total[j] = "-1" # 算過變-1
            j = num[int(store)] # j的值是num的index值
        print(*output)
        i = exist(total) 
        times += 1
    print("小團體數:",times)
    
if __name__ == "__main__" :
    main()