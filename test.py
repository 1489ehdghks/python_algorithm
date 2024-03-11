data = [10, 1, 5, 8, 7, 6, 4, 3, 2, 9]


def selection_sort(data):
    for i in range(0, len(data)-1):
        min_value = i
        for j in range(i+1, len(data)):
            if data[j] < data[min_value]:
                min_value = j
                print(j)
        data[i], data[min_value] = data[min_value], data[i]


selection_sort(data)
print(data)
