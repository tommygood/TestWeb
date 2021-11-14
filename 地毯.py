import matplotlib.pyplot as plt
#size = 要印出的地毯大小
def fractal(size):
    plotx,ploty=[],[]
    myFractal(size,0,0,plotx,ploty)
    plt.plot(plotx,ploty,'o')
    plt.show()   
#需要甚麼地毯呢?
#size : int of 大小
#x,y : int of 地毯左上角的座標
#plotx : list of 要畫的點x座標
#ploty :list of 要畫的點y座標
def myFractal(size,x,y,plotx,ploty):
    #多大的地毯一個人就可以畫了?
    if size == 1 :
        plotx.append(x)
        ploty.append(y)
        return
    #如果一個同學無法處理怎麼辦
    #找8個同學
    #765
    #8 4
    #123
    myFractal(size//3,x,y,plotx,ploty)
    myFractal(size//3,x+size//3,y,plotx,ploty)
    myFractal(size//3,x+2*size//3,y,plotx,ploty)
    myFractal(size//3,x+2*size//3,y+size//3,plotx,ploty)
    myFractal(size//3,x+2*size//3,y+2*size//3,plotx,ploty)
    myFractal(size//3,x+size//3,y+2*size//3,plotx,ploty)
    myFractal(size//3,x,y+2*size//3,plotx,ploty)
    myFractal(size//3,x,y+size//3,plotx,ploty)
    
def main():
    fractal(3**4)

if __name__ == '__main__':
    main()
    
