# 暗棋

# 隨機擺棋的位置
# 使用者輸入棋的座標
# 若棋是X, 代表翻開
# 不是X, 問他要移到上下左右
# 沒開的棋是0
# 有棋的位置就是1
# 沒有棋就是2
# 根據棋的大小給他一個值
# 被吃的棋, 該棋值改為0

from random import shuffle

def chinese(theChess):
    # 給棋子中文名稱
    wordChess = [[0 for c in range(8)] for r in range(4)]
    # 根據棋值, 給棋子中文名稱
    for i in range(4):
        for j in range(8):
            if theChess[i][j] == 0:
                wordChess[i][j] = " *卒"
            elif theChess[i][j] == 1:
                wordChess[i][j] = " #兵"
            elif theChess[i][j] == 10:
                wordChess[i][j] = " *包"
            elif theChess[i][j] == 11:
                wordChess[i][j] = " #炮"
            elif theChess[i][j] == 20:
                wordChess[i][j] = " *馬"
            elif theChess[i][j] == 21:
                wordChess[i][j] = " #傌"
            elif theChess[i][j] == 30:
                wordChess[i][j] = " *車"
            elif theChess[i][j] == 31:
                wordChess[i][j] = " #俥"
            elif theChess[i][j] == 40:
                wordChess[i][j] = " *象"
            elif theChess[i][j] == 41:
                wordChess[i][j] = " #相"
            elif theChess[i][j] == 50:
                wordChess[i][j] = " *士"
            elif theChess[i][j] == 51:
                wordChess[i][j] = " #仕"
            elif theChess[i][j] == 60:
                wordChess[i][j] = " *將"
            elif theChess[i][j] == 61:
                wordChess[i][j] = " #帥"
    return wordChess

def playChess(theChess, myChess, wordChess, situation, player, display, black, red, playerName):
    # 輪流下棋
    # 終止條件, 某一方亡棋達16隻
    if len(black) == 16:
        print(playerName[0]+" 贏了!")
        return
    if len(red) == 16:
        print(playerName[1]+"贏了!")
        return
    # 讓使用者輸入棋子座標
    if player == -1:
        print("輪到 "+playerName[0]+" 的回合")
    else:
        print("輪到 "+playerName[1]+" 的回合")
    # 檢查輸入
    value = 0
    while value == 0:
        print("請輸入要使用的棋子的座標, 並以空格隔開(橫,豎)")
        pos = input()
        if pos[1] == " ":
            r = int(pos[0])
            c = int(pos[2])
            value = 1
        else:
            print("你的輸入不符合規定, 請重新輸入")
    # 看該位置的狀況
    if situation[r][c] == 0: # 是未開的棋
        display1 = display[r][c] # 紀錄原位置顯示符號
        display[r][c] = " "+wordChess[r][c] # 將該棋翻開出來
        situation[r][c] = 1 # 改為已開
        print()
        print("     0    1    2    3    4    5    6    7")
        print("-------------------------------------------")
        for i in range(4):
            print(i, end = "")
            for j in range(8):
                print(display[i][j], end = "")
            print()
            print("-------------------------------------------")
        print()
        # 顯示亡棋
        print(playerName[1]+"的亡棋:")
        print(*black)
        print(playerName[0]+"的亡棋:")
        print(*red)
        # 提醒
        print("提醒: ＊ 代表是 "+playerName[1]+" 的棋子")
        print("提醒: ＃ 代表是 "+playerName[0]+" 的棋子")
        print("提醒: ● 代表是未翻開的棋子")
        print("提醒: Ｏ 代表是空格")
        print()
        # 換下一個人
        playChess(theChess, myChess, wordChess, situation, player*(-1), display, black, red, playerName)
        display[r][c] = display1
        situation[r][c] = 0
    elif situation[r][c] == 1: # 是已開的棋
        # 讓使用者輸入要移到上下左右哪個位置
        # 選到對方的棋
        if (myChess[r][c] % 10 == 0) and (player == -1):
            print("這支棋子是對手的, 請重新輸入")
            playChess(theChess, myChess, wordChess, situation, player, display, black, red, playerName)
            print()
        elif (myChess[r][c] % 10 == 1) and (player == 1):
            print("這支棋子是對手的, 請重新輸入")
            print()
            playChess(theChess, myChess, wordChess, situation, player, display, black, red, playerName)
        # 是自己的
        else:
            if theChess[r][c] == 10: # 是炮
                print("你這隻棋子是"+wordChess[r][c])
                print("若要移一格輸入 1, 若要跳格吃對方棋子輸入 2")
                x = int(input())
                if x == 1:
                    ans = [0,0,0,0]
                    if (r-1 >= 0) and (situation[r-1][c] == 2):
                        ans[0] = 1
                    elif (r+1 < 4) and (situation[r+1][c] == 2):
                        ans[1] = 2
                    elif (c-1 >= 0) and (situation[r][c-1] == 2):
                        ans[2] = 3
                    elif (c+1 < 8) and (situation[r][c+1] == 2):
                        ans[3] = 4
                    a = 0
                    print("你可以移到:")
                    for i in range(4):
                        if ans[i] == 1:
                            print("上方 ", end = "")
                            a = a + 1
                        elif ans[i] == 2:
                            print("下方 ", end = "")
                            a = a + 1
                        elif ans[i] == 3:
                            print("左方 ", end = "")
                            a = a + 1
                        elif ans[i] == 4:
                            print("右方 ", end = "")
                            a = a + 1
                    if a == 0:
                        print("無")
                        print("這顆棋子無法移動, 換一顆棋子吧")
                        playChess(theChess, myChess, wordChess, situation, player, display, black, red, playerName)
                    else:
                        nowChess = theChess[r][c]
                        nowWord = wordChess[r][c]
                        realValue = myChess[r][c]
                        theChess[r][c] = -1
                        wordChess[r][c] = " "
                        myChess[r][c] = -1
                        situation[r][c] = 2
                        display[r][c] = "   Ｏ"
                        print("輸入你要往哪裡移動(上,下,左,右)")
                        nextPos = input()
                        if nextPos == "上":
                            r = r - 1
                        elif nextPos == "下":
                            r = r + 1
                        elif nextPos == "左":
                            c = c - 1
                        elif nextPos == "右":
                            c = c + 1
                        theChess[r][c] = nowChess
                        wordChess[r][c] = nowWord
                        myChess[r][c] = realValue
                        situation[r][c] = 1
                        display[r][c] = " "+wordChess[r][c]
                        print()
                        print("    0    1    2    3    4    5    6    7")
                        print("-------------------------------------------")
                        for i in range(4):
                            print(i, end = "")
                            for j in range(8):
                                print(display[i][j], end = "")
                            print()
                            print("-------------------------------------------")
                        print()
                        print(playerName[1]+"的亡棋:")
                        print(*black)
                        print(playerName[0]+"的亡棋:")
                        print(*red)
                        print()
                        print("提醒: ＊ 代表是 "+playerName[1]+ "的棋子")
                        print("提醒: ＃ 代表是 "+playerName[0]+ "的棋子")
                        print("提醒: Ｘ 代表是未翻開的棋子")
                        print("提醒: Ｏ 代表是空格")
                        print()
                        playChess(theChess, myChess, wordChess, situation, player*(-1), display, black, red, playerName)
                else:
                    ans = [0,0,0,0]
                    # 炮移法不同
                    b = [0,0,0,0]
                    d = [0,0,0,0]
                    # 上方
                    for i in range(1,4):
                        if r-i >= 0 and b[0] < 2:
                            if (situation[r-i][c] != 2) and (b[0] == 0):
                                b[0] = b[0] + 1
                            elif (situation[r-i][c] == 1) and (b[0] == 1):
                                if (myChess[r][c] % 10) != (myChess[r-i][c] % 10): # 不能吃自己的
                                    b[0] = b[0] + 1
                                    ans[0] = 1
                                else:
                                    b[0] = b[0] + 1
                            d[0] = d[0] + 1
                    # 下方
                    for i in range(1,4):
                        if r+i < 4 and b[1] < 2:
                            if (situation[r+i][c] != 2) and (b[1] == 0):
                                b[1] = b[1] + 1
                            elif (situation[r+i][c] == 1) and (b[1] == 1):
                                if (myChess[r][c] % 10) != (myChess[r+i][c] % 10): # 不能吃自己的
                                    b[1] = b[1] + 1
                                    ans[1] = 2
                                else:
                                    b[1] = b[1] + 1
                            d[1] = d[1] + 1
                    # 左方
                    for i in range(1,8):
                        if c-i >= 0 and b[2] < 2:
                            if (situation[r][c-i] != 2) and (b[2] == 0):
                                b[2] = b[2] + 1
                            elif (situation[r][c-i] == 1) and (b[2] == 1):
                                if (myChess[r][c] % 10) != (myChess[r][c-i] % 10): # 不能吃自己的
                                    b[2] = b[2] + 1
                                    ans[2] = 3
                                else:
                                    b[2] = b[2] + 1
                            d[2] = d[2] + 1
                    # 右方 [r,c] = [0,1]
                    for i in range(1,8):
                        if c+i < 8 and b[3] < 2:
                            if (situation[r][c+i] != 2) and (b[3] == 0):
                                b[3] = b[3] + 1
                            elif (situation[r][c+i] == 1) and (b[3] == 1):
                                if (myChess[r][c] % 10) != (myChess[r][c+i] % 10): # 不能吃自己的
                                    b[3] = b[3] + 1
                                    ans[3] = 4
                                else:
                                    b[3] = b[3] + 1
                            d[3] = d[3] + 1
                    a = 0
                    print("你可以移到:")
                    for i in range(4):
                        if ans[i] == 1:
                            print("上方 ", end = "")
                            a = a + 1
                        elif ans[i] == 2:
                            print("下方 ", end = "")
                            a = a + 1
                        elif ans[i] == 3:
                            print("左方 ", end = "")
                            a = a + 1
                        elif ans[i] == 4:
                            print("右方 ", end = "")
                            a = a + 1
                    if a == 0:
                        print("無")
                        print("這顆棋子無法移動, 換一顆棋子吧")
                        playChess(theChess, myChess, wordChess, situation, player, display, black, red, playerName)
                    else:
                        nowChess = theChess[r][c]
                        nowWord = wordChess[r][c]
                        realValue = myChess[r][c]
                        theChess[r][c] = -1
                        wordChess[r][c] = " "
                        myChess[r][c] = -1
                        situation[r][c] = 2
                        display[r][c] = "   Ｏ"
                        print("輸入你要往哪裡移動(上,下,左,右)")
                        nextPos = input()
                        if nextPos == "上":
                            r = r - d[0]
                        elif nextPos == "下":
                            r = r + d[1]
                        elif nextPos == "左":
                            c = c - d[2]
                        elif nextPos == "右":
                            c = c + d[3]
                        # 黑方被吃一子
                        if (myChess[r][c] % 10 == 0) and (myChess[r][c] != -1):
                            black.append(wordChess[r][c])
                        # 紅方被吃一子
                        if (myChess[r][c] % 10 == 1) and (myChess[r][c] != -1):
                            red.append(wordChess[r][c])
                        theChess[r][c] = nowChess
                        wordChess[r][c] = nowWord
                        myChess[r][c] = realValue
                        situation[r][c] = 1
                        display[r][c] = " "+wordChess[r][c]
                        print()
                        print("    0    1    2    3    4    5    6    7")
                        print("-------------------------------------------")
                        for i in range(4):
                            print(i, end = "")
                            for j in range(8):
                                print(display[i][j], end = "")
                            print()
                            print("-------------------------------------------")
                        print()
                        print(playerName[1]+"的亡棋:")
                        print(*black)
                        print(playerName[0]+"的亡棋:")
                        print(*red)
                        print()
                        print("提醒: ＊ 代表是 "+playerName[1]+" 的棋子")
                        print("提醒: ＃ 代表是 "+playerName[0]+" 的棋子")
                        print("提醒: ● 代表是未翻開的棋子")
                        print("提醒: Ｏ 代表是空格")
                        print()
                        playChess(theChess, myChess, wordChess, situation, player*(-1), display, black, red, playerName)
            else:
                ans = [0,0,0,0]
                print("你這隻棋子是"+wordChess[r][c])
                # 上方
                if (r-1 >= 0) and (situation[r-1][c] != 0) and (chessValue(theChess, r, c, -1, 0, myChess) == True):
                    ans[0] = 1
                # 下方
                if (r+1 < 4) and (situation[r+1][c] != 0) and (chessValue(theChess, r, c, 1, 0, myChess) == True):
                    ans[1] = 2
                # 左方
                if (c-1 >= 0) and (situation[r][c-1] != 0) and (chessValue(theChess, r, c, 0, -1, myChess) == True):
                    ans[2] = 3
               # 右方
                if (c+1 < 8) and (situation[r][c+1] != 0) and (chessValue(theChess, r, c, 0, 1, myChess) == True):
                    ans[3] = 4
                a = 0
                print("你可以移到:")
                for i in range(4):
                    if ans[i] == 1:
                        print("上方 ", end = "")
                        a = a + 1
                    elif ans[i] == 2:
                        print("下方 ", end = "")
                        a = a + 1
                    elif ans[i] == 3:
                        print("左方 ", end = "")
                        a = a + 1
                    elif ans[i] == 4:
                        print("右方 ", end = "")
                        a = a + 1
                if a == 0:
                    print("無可移動的位置")
                    print("這顆棋子無法移動, 換一顆棋子吧")
                    playChess(theChess, myChess, wordChess, situation, player, display, black, red, playerName)
                else:
                    nowChess = theChess[r][c]
                    nowWord = wordChess[r][c]
                    realValue = myChess[r][c]
                    theChess[r][c] = -1
                    wordChess[r][c] = " "
                    myChess[r][c] = -1
                    situation[r][c] = 2
                    display[r][c] = "   Ｏ"
                    print("輸入你要往哪裡移動(上,下,左,右)")
                    nextPos = input()
                    if nextPos == "上":
                        r = r - 1
                    elif nextPos == "下":
                        r = r + 1
                    elif nextPos == "左":
                        c = c - 1
                    elif nextPos == "右":
                        c = c + 1
                    # 黑方被吃一子
                    if (myChess[r][c] % 10 == 0) and (myChess[r][c] != -1):
                        black.append(wordChess[r][c])
                    # 紅方被吃一子
                    if (myChess[r][c] % 10 == 1) and (myChess[r][c] != -1):
                        red.append(wordChess[r][c])
                    theChess[r][c] = nowChess
                    wordChess[r][c] = nowWord
                    myChess[r][c] = realValue
                    situation[r][c] = 1
                    display[r][c] = " "+wordChess[r][c]
                    print()
                    print("     0    1    2    3    4    5    6    7")
                    print("-------------------------------------------")
                    for i in range(4):
                        print(i, end = "")
                        for j in range(8):
                            print(display[i][j], end = "")
                        print()
                        print("-------------------------------------------")
                    print()
                    print(playerName[1]+"的亡棋:")
                    print(*black)
                    print(playerName[0]+"的亡棋:")
                    print(*red)
                    print()
                    print("提醒: ＊ 代表是 "+playerName[1]+" 的棋子")
                    print("提醒: ＃ 代表是 "+playerName[0]+" 的棋子")
                    print("提醒: ● 代表是未翻開的棋子")
                    print("提醒: Ｏ 代表是空格")
                    print()
                    playChess(theChess, myChess, wordChess, situation, player*(-1), display, black, red, playerName)
    elif situation[r][c] == 2: # 這個位置是空的
        print("這個位置沒有棋子, 請重新輸入")
        playChess(theChess, myChess, wordChess, situation, player, display, black, red, playerName)

def chessValue(theChess, r, c, row, col, myChess): # 比較棋值
    # 不能吃自己的
    if (myChess[r][c] % 10) != (myChess[r+row][c+col] % 10):
        # 如果是炮
        if theChess[r][c] == 10:
            theChess[r][c] = theChess[r][c] + 60
        # 如果我方是卒, 對方是帥
        elif (theChess[r][c] == 0) and (theChess[r+row][c+col] == 60):
            theChess[r][c] = theChess[r][c] + 70
        # 如果我方是帥, 對方是卒
        elif (theChess[r][c] == 60) and (theChess[r+row][c+col] == 0):
            theChess[r][c] = theChess[r][c] - 70
        # 我的棋值較大, 代表可以吃對方的棋
        if theChess[r][c] >= theChess[r+row][c+col]:
            return True
        # 我的棋值較小, 代表不能吃對方的棋
        else:
            return False
    else:
        return False

def main():
    # 簡介
    print()
    print("這是一款真正公平的暗棋遊戲")
    print("按下Enter來開始遊戲...")
    enter = input()
    # 顯示的棋盤
    display =[["   ●" for c in range(8)] for r in range(4)]
    # 棋值
    myChess = [0,0,0,0,0,1,1,1,1,1,10,10,11,11,20,20,21,21,30,30,31,31,40,40,\
    41,41,50,50,51,51,60,61] 
    # 洗牌
    shuffle(myChess)
    # 把棋值改成二維陣列
    theChess = [[0 for c in range(8)] for r in range(4)]
    myNewChess = [[0 for c in range(8)] for r in range(4)]
    for i in range(4):
        for j in range(8):
             theChess[i][j] = myChess[i*7+j+i]
             myNewChess[i][j] = myChess[i*7+j+i]
    # 給棋子中文名稱
    wordChess = chinese(theChess)
    # 紅方棋值要減1, 讓雙方棋值相等
    for i in range(4):
        for j in range(8):
            if (theChess[i][j] % 10) != 0 : # 如果是紅方
                theChess[i][j] = theChess[i][j] - 1 # 棋值要減1
    # 棋盤狀況表
    # 0是未翻開, 1是已翻開且有棋存在, 2是已翻開但無棋存在
    # 一開始都設0
    situation = [[0 for c in range(8)] for r in range(4)]
    for i in range(4):
        for j in range(8):
            situation[i][j] = 0
    # 紀錄亡棋
    black = [] # 黑方亡棋
    red = [] # 紅方亡棋
    # 玩家代碼
    player = 1
    # 玩家名稱
    playerName = [0,0]
    print("請輸入玩家姓名")
    print("player1(*): ", end = "")
    playerName[1] = input()
    print("player2(#): ", end = "")
    playerName[0] = input()
    # 顯示棋盤
    print("遊戲開始!")
    print()
    print("     0    1    2    3    4    5    6    7")
    print("-------------------------------------------")
    for i in range(4):
        print(str(i)+"   ●   ●   ●   ●   ●   ●   ●   ●")
        print("-------------------------------------------")
    print()
    print("提醒: ＊ 代表是"+playerName[1]+"的棋子")
    print("提醒: ＃ 代表是"+playerName[0]+"的棋子")
    print("提醒: ● 代表是未翻開的棋子")
    print("提醒: Ｏ 代表是空格")
    print()
    # 如果亡棋有16隻代表輸了
    # 沒結束就輪流下棋
    playChess(theChess, myNewChess, wordChess, situation, player, display, black, red, playerName)

if __name__ == "__main__":
    main()