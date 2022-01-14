def bubble_sort(t):
    for i in range(len(t)):
        for j in range(0, len(t) - i - 1):
            if t[j] > t[j+1]:
                t[j], t[j+1] = t[j+1], t[j]
    return t
  
def selection_sort(t):
    for i in range(len(t)):
        min = i
        for j in range(i, len(t)):
            if t[j] < t[min]:
                t[j], t[min] = t[min], t[j]
    return t

def insertion_sort(t):
    for i in range(2, len(t)):
        e = t[i]
        j = i - 1
        while j >= 0 and t[j] > e:
            t[j+1] = t[j]
            j-=1
        t[j+1] = e
    return t
