from random import randint
from time import time
import matplotlib.pyplot as plt

def main():
    # printList = False
    # n = int(input("Enter the list size: "))
    # values = []
    # for i in range(n):
    #     values.append(randint(1,5*n))
    # if printList:
    #     print(values)
    # mergeSort(values)
    # if printList:
    #     print(values)

    x = [100, 200, 400, 800, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    # x = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
    # x = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    y = []

    y2 = []
    y3 = []
    y4 = []
    for j in x:
        values = []
        for i in range(j):
            values.append(randint(1, j))

        startTime = time()
        insertionSort(values)
        endTime = time()
        y.append(endTime - startTime)

        startTime = time()
        selectionSort(values)
        endTime = time()
        y2.append(endTime - startTime)

        startTime = time()
        mergeSort(values)
        endTime = time()
        y3.append(endTime - startTime)

        startTime = time()
        bubbleSort(values)
        endTime = time()
        y4.append(endTime - startTime)

    plt.plot(x, y4, label="Bubble Sort")
    plt.plot(x, y3, label="Merge Sort")
    plt.plot(x, y2, label="Selection Sort")
    plt.plot(x, y, label="Insertion Sort")

    legend = plt.legend(loc='best', shadow=True, fontsize='medium')
    legend.get_frame().set_facecolor('#00FFCC')

    plt.ylabel('Time')
    plt.xlabel('Number of Items')
    plt.show()

def selectionSort(values):
    for i in range(len(values)):
        minPos = minimumPosition(values, i)
        temp = values[minPos]
        values[minPos] = values[i]
        values[i] = temp

def minimumPosition(values, start):
    minPos = start
    for i in range(start + 1, len(values)):
        if values[i] < values[minPos]:
            minPos = i

    return minPos

def insertionSort(values):
    for i in range(1, len(values)):
        next = values[i]

        # Move all larger elements up
        j = i
        while j > 0 and values[j - 1] > next:
            values[j] = values[j - 1]
            j -= 1

        # Insert the element
        values[j] = next

def mergeSort(values):
    if len(values) <= 1:
        return
    mid = len(values) // 2
    first = values[ : mid]
    second =  values[mid: ]
    mergeSort(first)
    mergeSort(second)
    mergeLists(first, second, values)

def mergeLists(first, second, values):
    iFirst = 0 # Next element to consider in the first list
    iSecond = 0 # Next element to consider in the second list
    j = 0

    # As long as neither iFirst nor iSecond is past the end, move
    # the smaller element into values

    while iFirst < len(first) and iSecond < len(second):
        if first[iFirst] < second[iSecond]:
            values[j] = first[iFirst]
            iFirst += 1
        else:
            values[j] = second[iSecond]
            iSecond += 1

        j += 1

    # Note that only one of the two loops below copies entries
    # Copy any remaining entries on the first list
    while iFirst < len(first):
        values[j] = first[iFirst]
        iFirst += 1
        j += 1

    # Copy any remaining entries of the second list
    while iSecond < len(second):
        values[j] = second[iSecond]
        iSecond += 1
        j += 1

def bubbleSort(values):
    for passnum in range(len(values) - 1, 0, -1):
        for i in range(passnum):
            if values[i] > values[i + 1]:
                temp = values[i]
                values[i] = values[i + 1]
                values[i + 1] = temp

if __name__ == '__main__':
    main()