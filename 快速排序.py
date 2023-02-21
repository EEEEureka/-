def partition(arr,left,right):
    i = left
    j = right
    mid = arr[left]
    while i != j:       #如果指针没有重合
        while i < j and arr[j] > mid:   #先从右侧指针开始向左移动，如果比选中的值大，才可以向左移动，否则不移动
            j -= 1
        while i < j and arr[i] <= mid:  #再从左侧指针开始向右移动，如果比选中的值小，才可以向右移动，否则不移动
            i += 1
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]   #上述的两种情况都进入了否则，那么就交换两者的值后，继续这样进行
    arr[left],arr[i] = arr[i],arr[left]     #将数组中此时最左边的值和两个指针到达同一位置时对应的值进行交换
    return i #返回指针位置

def quicksort(arr,left,right):
    if (left >= right):     #如果数组中只有一个元素或者没有元素，则无需排序，直接 return 出去
        return
    mid_index = partition(arr,left,right)
    quicksort(arr,left,mid_index - 1)
    quicksort(arr, mid_index + 1,right)

if __name__ == '__main__':
    arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quicksort(arr, 0, len(arr) - 1)   #0代表数组最左边  len(arr) - 1代表最右边
    print(arr)