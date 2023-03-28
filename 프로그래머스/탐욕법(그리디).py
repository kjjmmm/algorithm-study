def solution(n, lost, reserve):
    
    cnt=0

    lost = list(set(lost) - (set(lost) & set(reserve)))
    reserve = list(set(reserve) - (set(lost) & set(reserve)))

    for i in range(len(lost)):
        
        for j in range(len(reserve)):
            
            if abs(lost[i]-reserve[j])==1:
                cnt+=1
                del reserve[j]
                break

    print(n)
    print(len(lost))
    print(cnt)

    print(n-len(lost)+cnt)

solution(5,[2,4],[3])
        