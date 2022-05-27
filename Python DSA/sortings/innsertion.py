def insertion_sort(elements):
    for i in range(1, len(elements)):
        arey = elements[i]
        j = i-1

        while j>=0 and elements[j] > arey:
            elements[j+1] = elements[j]
            j = j - 1
        elements[j+1] = arey    


if __name__ == "__main__":
    elements = [0,23,-728,5,9,2,1,76,88,-12,-45,51,0]

    insertion_sort(elements)
    print(elements)