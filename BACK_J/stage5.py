def ques1():
    def solve(a):
        return sum(a)

def ques2():
    arr=[]
    for i in range(1,10001):
        str_i=str(i)
        result = int(str_i)
        for j in range(len(str_i)):
            result+=int(str_i[j])
        arr.append(result)
    arr.sort()
    arr2=[]
    for i in range(1,10001):
        arr2.append(i)

    arr3 = list(set(arr2)-set(arr))
    arr3.sort()

    for i in range(len(arr3)):
        print(arr3[i])

def ques3():
    n = int(input())

    result = 0

    for i in range(1,n+1):

        if i < 100 : 
            result+=1 
            continue;

        tmp = str(i)
        cha=0
        for j in range(len(tmp)-1):
            tmp_cha = int(tmp[j+1])-int(tmp[j])
            if j!=0 and cha!=tmp_cha :
                break;
            cha = int(tmp[j+1])-int(tmp[j])
            if j==len(tmp)-2 :
                result+=1

    print(result)

ques3()






    
