fn="108_student.csv"
infile = open(fn, "r",encoding="UTF-8")
line=infile.readline().split(',')
print(line[1],line[4])
print('')

counter = {} 
for i in range(794):
    
    line=infile.readline().split(',')
    name=line[1]
    nums=int(line[4])
    
    if name in counter:
        counter[name] += nums
    else:
        counter[name] = nums
        
a = list(counter.items())

def f(x):
   return x[1]

a.sort(key=f,reverse=True)

first=0
print('前十名')
for key, value in a:
    first +=1
    if first>10:
        break
    print("{} {}".format(key, value))       
print('')

last=0
print('後十名')
for key, value in a:
    last +=1
    if last>142:
        print("{} {}".format(key, value))
    if first>152:
        break

infile.close()





