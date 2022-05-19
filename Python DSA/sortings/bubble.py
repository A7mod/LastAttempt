def bubble_sort(elements):
    size = len(elements)

    for k in range(size-1):
        for i in range(size-k-1):
            if elements[i] > elements[i+1]:
                tmp = elements[i]
                elements[i] = elements[i+1]
                elements[i+1] = tmp



if __name__ == "__main__":
    elements = [5,9,2,1,76,88,-12,-45,51,0]

    bubble_sort(elements)
    print(elements)