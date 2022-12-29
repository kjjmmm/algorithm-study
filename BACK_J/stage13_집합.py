
def ques1():

    result=[]
    n = int(input())
    arr1 = set(input().split())

    m = int(input())
    arr2 = input().split()

    for i in arr2:
        if i in arr1 : 
            result.append(1)
        else :
            result.append(0)

    print(*result)
            
ques1()
        


    