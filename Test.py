import openpyxl
workbook = openpyxl.load_workbook('HW12.xlsx') # 開啟檔案
file = workbook["money"]
total = {"食":0,"衣":0,"住":0,"行":0,"育":0,"樂":0} # 先創好dic
workbook.create_sheet(title = "newFile") # 創新分頁
file2 = workbook["newFile"]
for i in range(34):
    i += 1 # 從A1開始
    if i == 1 : # 項目欄不要
        continue
    pos = "A"+str(i) # 要找的位置index
    pos2 = "B"+str(i) # 去找到他的數量
    if file[pos].value in total : # 如果是要找的       
        total[file[pos].value] += file[pos2].value # 加進字典裡
    else :
        print("第"+str(i)+" row分類錯誤。") # 印出
for i in total: # 印出來
    print(i+":"+str(total[i])+"元")
n = 0 # 格子的位置
for i in total :
    n += 1
    pos = "A"+str(n) # index位置
    file2[pos].value = i
    pos2 = "B"+str(n)
    file2[pos2].value = total[i]
workbook.save("HW12.xlsx") # 存檔