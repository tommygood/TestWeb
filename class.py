class catSlave():
    def __init__(self,name):
        self.name = name
        self.cats = []
    def __add__(self,n):
        for i in range(n):
	        self.cats.append('沒名')
    def addCat(self,cname):
	    self.cats.append(cname)
    def print(self):
	    print(self.name)
	    print(*self.cats)
def main():
    老魚 = catSlave('魚')
    老魚.addCat('鯊魚')
    老魚.addCat('孔雀魚')
    老魚.addCat('吳郭魚')
    老魚 + 3
    老魚.print()
	
main()
