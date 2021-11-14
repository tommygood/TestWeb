def findSol(data,first,second):
    mysol(data,first,second,0)



def mySol(data,first,second,pos):
    if pos == len(data):
        if int(data[:first]) * int(data[first:first+second]) == int(data[first
            print(data[:first],'*',data[first:first+second],'=',data[first+second
        return
    if data[pos] == '?' :
        for num in range(10) :
            mySol(data[:pos]+str(num)+data[pos+1:],first,second,pos+1)
    else :
        mySol(data,first,second,pos+1)

def main():
    
