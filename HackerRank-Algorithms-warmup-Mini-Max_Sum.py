def sort(arr):
    new_arr = arr
    n = len(new_arr)

    swapped = True
    while swapped:
        swapped = False
        for i in range(len(new_arr) - 1):
            if new_arr[i] > new_arr[i + 1]:
                swapped = True
                new_arr[i], new_arr[i + 1] = new_arr[i + 1], new_arr[i]
    
    return new_arr

def miniMax_sum(arr):
    sorted_arr = sort(arr)
    n = len(sorted_arr)
    Min = 0 
    for i in range(0, n - 1):
        Min += sorted_arr[i]
    
    Max = 0
    for i in range(1, n):
        Max += sorted_arr[i]
    
    print(Min, Max)

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    miniMax_sum(arr)

