
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

print("before: ", array)
selection_sort(array)
print("after", array)

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
  return arr

print(insertion_sort(arr))
      


