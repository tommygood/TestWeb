a = input().split()
for i in range(34):
        if i < 9 :
            print(str(a[i])+" "+str(i+1)+"萬"+str(i))
        if 8 < i < 18 :
            print(str(a[i])+" "+str(i-8)+ "筒"+str(i))
        if 17 < i < 27 :
            print(str(a[i])+" "+str(i-17)+"條"+str(i))
        if i == 27 :
            print(str(a[i])+"東")
        if i == 28 :
            print(str(a[i])+"西")
        if i == 29 :
            print(str(a[i])+"南")
        if i == 30 :
            print(str(a[i])+"北")
        if i == 31 :
            print(str(a[i])+"中")
        if i == 32 :
            print(str(a[i])+"發")
        if i == 33 :
            print(str(a[i])+"白")
