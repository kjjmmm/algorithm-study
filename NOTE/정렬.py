
# 버블 정렬(Bubble Sort)
# 시간 복잡도 O(N*N)
array = [9,8,7,6,5,4,3,2,1]

def bubble_sort(array):
    n = len(array) # 9
    cnt = 0
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            cnt+=1
            print(array)
    print(cnt)

# print("before", array)
# bubble_sort(array)
# print("after", array)

# 선택 정렬(Selection Sort)
# 한 바퀴 돌 때 가장 작은 값을 찾아 맨 앞과 교환하는 방식의 정렬.
# 앞에서부터 정렬해나가는 특성을 가지고 있고 버블 정렬과 마찬가지로 최악의 성능을 가진 알고리즘.
# 시간 복잡도 O(N*N) 
# 그래도 버블 정렬보다 좋다.

array = [8,4,6,2,9,1,3,7,5]

def selection_sort(array):
    n = len(array)
    for i in range(n):

        min_index = i # 맨앞의 index 값을 min_index 로 잡아놓음.

        for j in range(i+1, n):
            
            if array[min_index] > array[j]:
                min_index = j # 작은 수가 앞으로 가야하기 때문

        array[i], array[min_index] = array[min_index], array[i] # 가장 작은수와 index 를 이용하여 변경
        print(array[:i+1])

# print("before: ", array)
# selection_sort(array)
# print("after", array)

# 이것은 삽입 정렬이다.
# - 삽입정렬의 시간복잡도는 O(N²)로, 앞 글에서 배운 선택정렬과 비슷한 시간이 소요된다. 
# - 하지만, 삽입정렬은 데이터가 정렬이 되어있는 경우 매우 빠르게 동작하며, 가장 빠른 경우 O(N)의 복잡도를 가진다.
# - 이어서 배울 퀵 정렬 알고리즘과 비교했을 때에도, 일반적으로 퀵정렬이 효율적이나 데이터가 정렬되어있을 경우 삽입정렬이 더 효율적이다. 

arr = [9,8,7,6,5,4,3,2,1]

def insertion_sort(arr):
  for i in range(1,len(arr)):
    for j in range(i,0,-1):
      if arr[j-1] > arr[j] :
        arr[j-1], arr[j] = arr[j], arr[j-1]
      else : 
         break
  return arr

# print(insertion_sort(arr))

# 삽입 정렬 2 - 최적화

def best_insertion_sort(arr):
   
    for i in range(1, len(arr)):
        j = i
        # 정렬 할것이 있으면 계속한다. 하지만 앞에 더 작은 수가 있다면 정렬할 필요가 없겠지 -> while 문 False 탈출
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr

# print(best_insertion_sort(arr))


array = [5,7,9,0,3,1,6,2,4,8]

# 퀵 정렬
# 시간 복잡도 O(NlogN) - 평균 / 최악 N**2
def quick_sort(array, start, end):
   
    if start >= end : return # 원소가 1개인 경우
    pivot = start # 피벗은 첫 요소
    left, right = start + 1, end

    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복 - 피벗보다 큰 데이터를 찾거나, left 가 end 보다 커질때 탈출
        while left <= end and array[left] <= array[pivot] :
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # 엇갈렸다면 작은 데이터와 피벗을 교체
        if left > right :
            array[right], array[pivot] = array[pivot], array[right]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else :
            array[left], array[right] = array[right], array[left]
    # 재귀
    quick_sort(array, start, right - 1)
    quick_sort(array, right+1, end)

# quick_sort(array, 0, len(array) - 1)
# print('quick',array)


# 계수 정렬 - 카운팅 정렬 O(n+k)
def counting_sort(arr):
    max_value = max(arr)
    m = max_value + 1

    count = [0] * m
    sorted_arr=[]

    for a in arr :
        count[a] += 1

    for i in range(len(count)):
        for j in range(count[i]):
            sorted_arr.append(i)
    return sorted_arr

print(counting_sort(arr))