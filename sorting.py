from random import randint
from time import time
import matplotlib.pyplot as plt

def main():
    printList = False
    #n = int(input("Enter the list size: "))

    x = [100, 200, 400, 800, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    y = []
    for j in x:
        values = []
        for i in range(j):
            values.append(randint(1,j))
        if printList:
            print(values)
        startTime = time()
        selectionSort(values)
        endTime = time()
        if printList:
            print(values)
        print("Elapsed time: %.3f" % (endTime - startTime))
        y.append((endTime - startTime))

    plt.plot(x, y)
    plt.plot(x, y, label="Selection Sort")
    legend = plt.legend(loc='upper center', shadow=True, fontsize='x-large')
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

if __name__ == '__main__':
    main()