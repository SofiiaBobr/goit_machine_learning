## Завдання .tim
#Python має дві вбудовані функції сортування: `sorted` і `sort`. Функції сортування Python 
#використовують Timsort — гібридний алгоритм сортування, що поєднує в собі сортування 
# злиттям і сортування вставками.

#Порівняйте три алгоритми сортування: злиттям, вставками та Timsort за часом виконання. 
# Аналіз повинен бути підтверджений емпіричними даними, отриманими шляхом тестування 
# алгоритмів на різних наборах даних. Емпірично перевірте теоретичні оцінки складності алгоритмів,
#наприклад, сортуванням на великих масивах. Для заміру часу виконання алгоритмів використовуйте 
# модуль `timeit`.

#Покажіть, що поєднання сортування злиттям і сортування вставками робить алгоритм 
# Timsort набагато ефективнішим, і саме з цієї причини програмісти, в більшості випадків, 
# використовують вбудовані в Python алгоритми, а не кодують самі. Зробіть висновки.

import random
import timeit

def insretion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i -1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            
        arr[j+1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2

        L,R = arr[:mid], arr[mid:]
        merge_sort(L); merge_sort(R)
        i = j = k = 0
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                arr[k] = L[i]
                i+= 1
            else:
                arr[k] = R[j]
                j+= 1

        while i < len(L):
            arr[k] = L[i]
            k+= 1
            i+= 1

        while j<len(R):
            arr[k] = R[j]
            k+= 1
            j+= 1

if __name__ == "__main__":
    data = [random.randint(0,1_000_000) for _ in range(10000)]
    time_ins = timeit.timeit(lambda: insretion_sort(data.copy()), number=10)
    time_mer = timeit.timeit(lambda: merge_sort(data.copy()), number=10)
    time_timsort = timeit.timeit(lambda: sorted(data.copy()), number=10)
    print(f'inseption sort {time_ins:.5f}s')
    print(f'merge sort {time_mer:.5f}s')
    print(f'timesort {time_timsort:.5f}s')