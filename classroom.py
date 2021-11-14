#學號:109213059
#姓名:王冠權
#題目連結 : https://hackmd.io/7b_uqvd2SNKUtY5p1mXxNg?view

def count(n,mp,pmp): #計算教室內被點到低於 3 次(不包含 3) 的學生
    student = 0 #低於3次的學生
    ans = [] #剩下同學的座號
    for i in range(n):  #每個檢查
        for k in range(n):
            if pmp[i][k] < 3: #同學被點到低於3次
                student = student + 1
                ans = ans + [mp[i][k]+1] #剩下同學
    if student < 5 : #小於5就印出來
        answer = '' #把答案變字串
        for i in ans : #一個一個加出來
            answer = answer + str(i) + ' '
        print(answer)
        return False   #終止迴圈
    else:
        return True  #繼續迴圈
        
def loc(n): #從1開始的地圖
    mp = []  #mp = 從1開始的地圖
    for i in range(n):
        num = [] #每一列的數字
        for k in range(n):
            num.append(k+i*n) #第一個數字會是要*n
        mp.append(num) #加起來
    return mp
    
def cross(n,s,pmp): #玩大十字 (算大家被點名的次數)
    r = (s-1) // n #第幾列 , 從1開始的
    c = (s % n) - 1 #第幾行
    for i in range(n):  #同行,列加1
        pmp[r][i] = pmp[r][i] + 1
        pmp[i][c] = pmp[i][c] + 1
    pmp[r][c] = pmp[r][c] - 1 #會重複算到
    return pmp
    
def main(): #主程式
    n = int(input())  #幾成幾
    final = True #final 先設為True 
    op = [[0 for i in range(n)]for i in range(n)] #op = 0的地圖
    while final : 
         s = int(input()) #點到哪個同學
         mp = loc(n)  #一開始從1開始的地圖
         pmp = cross(n,s,op) #每個位置被點到的次數的地圖,一開始先設為0
         final = count(n,mp,pmp) #final = 如果算出來是小於5個同學 
    
if __name__ == '__main__' :
    main()
