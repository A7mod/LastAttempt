def selection_sort(arr):
    size = len(arr)

    for i in range(size):
        min = i
        for j in range(min+1, size):
            if arr[j] < arr[min]:
                min = j

        if i != min:
            arr[i], arr[min] = arr[min], arr[i]        

    
#selection sort can be done in two ways apparantly. In 

if __name__ == "__main__":
    elements = [5,9,2,1,76,88,-12,-45,51,0]

    selection_sort(elements)
    print(elements)