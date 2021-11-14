class good():
    def __init__(self,name):#__init__是起手式,會直接執行。
        self.name = name #變數前面加上self(可以別的)就可以通用到這個class的其他函數裡面
        self.list = [1,2,3]
    def a(self,word) :
        self.words = self.name + word
        print(self.name,self.words)
    def __add__(self,num):
        self.list.append(3*num)
    def b(self):
        print(self.list)
def main():
    n = good('tommy')  #一開始一個就好，不要good('tommy').a('great')之類的
    n + 3
    n.b()
    
    
     
main()