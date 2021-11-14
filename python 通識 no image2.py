import tkinter as tk
import sys

def chart(): #圖表
    a = tk.Tk()
    a.title('python 通識')
    a.geometry('8000x4000')
    return a

def percent(date,a,line):  #長條圖的比例  #date = 年或月
    for f in line :  #line = 單年或全年份
        fm = tk.Frame(a)
        fm.grid(sticky='w')  #向左貼齊
        text = tk.Label(fm, bg='black', fg='white', 
        text =(date[line.index(f)],':',('%.3f' % f ),'%'), \
             font=('微軟正黑體', 10), padx=f*80,pady=8) #*80比較清楚
        text.grid(sticky='w') #向左貼齊
        
def allYear():  
    total = [[] for i in range(19)]  #總共有19年
    file = open('90-108年失業率(月分計).txt','r')
    word = file.readline() #第一行是科目
    for k in range(len(total)):  #每年分別用一個list儲存
        for i in range(12):   #每年12個月
            word = file.readline()  
            word = word.split()
            total[k] = total[k] + word
    file.close()
    return total

def unemploy(total,y,stat):  #失業率年平均 #y=search
    if type(y) == int: #單年
        mon = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept',\
               'Oct','Nov','Dec'] #月份
        employ = 0 #employ = 當年度的失業率加總
        sep = []   #sep = 每個月各別的失業率
        y = y - 90  #y = 那一年
        for i in range(-1,36,3): #失業率在第三格 , 1年12個月
            if i > 0 :
                employ = employ + float(total[y][i])
                sep.append(float(total[y][i]))
        unemployment = employ / 12   #unemployment = 該年的平均失業率
        extreB = 0 #最大
        extreS = 8 #最小
        for i in range(len(sep)) :
            print(i+1,sep[i])
            extreB = max(extreB,sep[i]) #最大
            extreS = min(extreS,sep[i]) #最小
        print('本年的平均失業率為',unemployment,'%')
        print('本年中失業率最高的月份是',sep.index(extreB)+1,'月，失業率為',extreB,'%'\
              ,'\n失業率最低的月份是',sep.index(extreS)+1,'月，失業率為',extreS,'%')
        return mon,sep,extreB,extreS
    elif y == 'total' or y == 'Misery index':  #全年份
        totalUnem = []   #全部的每年失業率
        for l in range(len(total)): #總共有幾年
            tUnemploy = 0 #每一年的失業率
            for i in range(-1,36,3): #失業率在第三格
                if i > 0 :
                    tUnemploy = tUnemploy + float(total[l][i])
            totalUnem.append(tUnemploy / 12)
        extreB = 0 #最大
        extreS = 8 #最小
        year = [i for i in range(90,109)]
        if y == 'Misery index' :
            search = [] #每年分別的通膨率
            s = []  #每年分別的痛苦指數
            for i in range(len(stat)):
                search = search + [stat[i][2]] #在檔案第3個位置
            for i in range(len(total)):  #通膨+失業率
                s = s + [totalUnem[i] + float(search[i])] 
            for i in range(len(s)) :  
                print(90+i,s[i])    #還要印年份
                extreB = max(extreB,s[i]) #最大
                extreS = min(extreS,s[i]) #最小
            print('痛苦指數最高的年份是',90+s.index(extreB),'年，痛苦指數為',\
              extreB,'%','\n痛苦指數最低的年份是',90+s.index(extreS),'年，痛苦指數為',extreS,'%')
            return year,s,extreB,extreS
        for i in range(len(totalUnem)) :  #還要印年份
            print(90+i,totalUnem[i])
            extreB = max(extreB,totalUnem[i]) #最大
            extreS = min(extreS,totalUnem[i]) #最小
        print('失業率最高的年份是',90+totalUnem.index(extreB),'年，失業率為',\
              extreB,'%','\n失業率最低的年份是',90+totalUnem.index(extreS),'年，失業率為',extreS,'%')
        return year,totalUnem,extreB,extreS
    
def stat(): #開通膨
    total = [[] for i in range(19)]
    file = open('統計資料年分計.txt','r')
    word = file.readline()
    for k in range(len(total)):
        word = file.readline()  
        word = word.split()
        total[k] = total[k] + word
    file.close()
    return total

def find(): #要全年份的還是單年
    while True :
        print('''您想搜尋什麼資料呢？民國90－108年每一個年度的平均失業率、
單一年份每月平均失業率呢，或者痛苦指數？(輸入total(t)或single(s))或Misery index(m)''')
        search = input().lower()
        if search.startswith('t')  :
            return 'total'
        elif search.startswith('s') :
            print('您想搜尋哪一個年份的資料呢？(請輸入90-108)')
            year = str(input())
            if not year.isdigit() :
                continue  #不是數字就再問一次
            return int(year) if int(year) < 109 and int(year) >= 90 \
                   else sys.exit()
        elif search.startswith('m'):
            return 'Misery index'
        else :
            if search == 'quit' :
                sys.exit()
            continue #search不是t開頭或是s開頭再問一次
        
def main():
    search = find()   #搜尋什麼
    total = allYear()  #全部的數據
    sta = stat()  #通膨數據
    date,line,extreB,extreS = unemploy(total,search,sta) #line = 條狀圖要用全年份還是單年 date=月 年
    a = chart()  #圖
    percent(date,a,line)
    
if __name__ == '__main__' :
    main()



