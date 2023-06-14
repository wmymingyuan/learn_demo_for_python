# 插入排序
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 58]
    insertionSort(arr)
    print("排序后的数组:")
    for i in arr:
        print(i)
