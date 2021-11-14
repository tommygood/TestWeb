def combine(let,num):
    ans = ''
    answer = []
    for i in let :
        ans = i
        for l in let :
            ans = i + l
            for k in let :
                ans = ans + k
                answer.append(ans)
                ans = i + l
    return answer                
def order(total):
    answer = []
    for i in total :
        if i not in answer :
            answer.append(i)
    return(answer)

def main():
   print(*order(combine('ABCDE',3)))
    
main()
