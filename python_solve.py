import random

def bubble_sort(arr):
    length = len(arr)

    for i in range(0, length-1): #якщо проходити до n, я не до n-1, то останній цикл виконається два рази
        for j in range(0, length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

l = []

amount = int(input("Введіть кількість випадкових чисел, які потрібно сгенерувати"))

for i in range(amount):
    l.append(random.randint(10,100))

#l = bubble_sort(l)
#print(l)

with open('result.txt', 'w') as f:
    phrase = (f'You have input this amount of numbers to be generated: {amount}\n')
    f.write(phrase)
    f.write(f"Generated numbers: {l}\n")
    f.write(f"Sorted numbers: {bubble_sort(l)}\n")

