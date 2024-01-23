def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


if __name__ == '__main__':
    array_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    sorted_array = insert_sort(array_list)
    print("排序结果：", sorted_array)
