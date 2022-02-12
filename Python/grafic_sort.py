import pygame, random, sys

window = pygame.display.set_mode([0, 0], pygame.RESIZABLE)

id = 0
right = 1
stop = False
try:
    which = sys.argv[1]
    width = int(sys.argv[2])
except:
    print("\npython grafic_sort.py {which sort} {width of post}\nYou can choose from bubble, random, quicksort\n")
    exit()
how_many = round(window.get_width() / width)
post = pygame.Surface([width, window.get_height()])
post.fill([0, 0, 0])
def draw_post(x, y):
    window.blit(post, [x, y])
array = []
for i in range(how_many):
    array.append(random.randint(1, window.get_height()))

def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


def quickSort(arr, low, high):
    for i in range(how_many):
        draw_post(i*width, window.get_height() - array[i])
    pygame.display.flip()
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
    stop = True

def is_sort():
    for i in range(len(array)-1):
        if array[i] > array[i + 1]:
            break
    stop = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                exit()
    window.fill([255, 255, 255])
    for i in range(how_many):
        draw_post(i*width, window.get_height() - array[i])
    if not stop:
        if which == "bubble":
            if id >= how_many - right:
                right += 1
                id = 0
            if array[id] > array[id + 1]:
                array[id], array[id + 1] = array[id + 1], array[id]
            id+=1
            is_sort()
        elif which == "random":
            los = random.randint(0, how_many-2)
            if array[los] > array[los + 1]:
                array[los], array[los + 1] = array[los + 1], array[los]
            is_sort()
        elif which == "quicksort":
            quickSort(array, 0, len(array)-1)
    pygame.display.flip()
