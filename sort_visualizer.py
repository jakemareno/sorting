import random
from turtle import Turtle, Screen, tracer, update, done, colormode
from time import sleep

NUMBER_OF_ELEMENTS = 30
WIDTH = 510
HEIGHT = WIDTH
SCALE = int(WIDTH/NUMBER_OF_ELEMENTS)
DELAY = 0.001
PAUSE = 0.5
SHUFFLES = 2

tracer(0,0)
colormode(255)


screen = Screen()
screen.bgcolor("black")
screen.title("Sorting!")
screen.setup(WIDTH+SCALE*3, HEIGHT+SCALE*3)

t = Turtle()
t.color("black")
t.setheading(90)
t.pensize(SCALE)
t.speed(0)
t.penup()


def set_nums():
    nums = []

    for i in range(1, NUMBER_OF_ELEMENTS + 1):
        nums.append(i)
    
    draw_nums(nums)

    return nums



def draw_nums(nums):
    t.clear()
    for i in range(len(nums)):
        red = int(255-nums[i]/NUMBER_OF_ELEMENTS*255)
        green = int(abs(128-nums[i]/NUMBER_OF_ELEMENTS*255))
        blue = int(nums[i]/NUMBER_OF_ELEMENTS*255)
        t.setpos(SCALE*i - WIDTH/2, -HEIGHT/2)
        t.color((red, green, blue))
        t.pendown()
        t.forward(nums[i]*SCALE)
        t.penup()

    sleep(DELAY)
    update()


def draw_nums_highlight(nums, highlight):
    t.clear()
    for i in range(len(nums)):
        red = int(255-nums[i]/NUMBER_OF_ELEMENTS*255)
        green = int(abs(128-nums[i]/NUMBER_OF_ELEMENTS*255))
        blue = int(nums[i]/NUMBER_OF_ELEMENTS*255)
        t.setpos(SCALE*i - WIDTH/2, -HEIGHT/2)
        t.color((red, green, blue))
        if i == highlight:
            t.color((0,255,0))
        t.pendown()
        t.forward(nums[i]*SCALE)
        t.penup()

    sleep(DELAY)
    update()


def shuffle_nums(nums):
    for i in range(len(nums)*SHUFFLES):
        i = random.randint(0, NUMBER_OF_ELEMENTS-1)
        j = random.randint(0, NUMBER_OF_ELEMENTS-1)
        nums[i], nums[j] = nums[j], nums[i]
        draw_nums(nums)

    return nums



def bubble_sort(nums: list) -> list:
    swaps = 0

    for i in range(len(nums)):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swaps += 1
                draw_nums_highlight(nums, j+1)

    print(swaps)
    return nums


def insertion_sort(nums):
    for i in range(1, len(nums)):
        key_item = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key_item:
            nums[j + 1] = nums[j]
            draw_nums_highlight(nums, j+1)
            j -= 1
        nums[j + 1] = key_item
        draw_nums_highlight(nums, j+1)
    return nums


def merge(left, right):
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []

    index_left = index_right = 0
    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break
    return result


def merge_sort(nums):
    if len(nums) < 2:
        return nums
    midpoint = len(nums) // 2
    return merge(left=merge_sort(nums[:midpoint]), right=merge_sort(nums[midpoint:]))


def shaker_sort(nums):
    i = len(nums) - 1
    while i > (len(nums)/2):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                draw_nums_highlight(nums, j+1)
        j = i
        while j > len(nums) - i:
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
                draw_nums_highlight(nums, j-1)
            j -= 1
        i -= 1

    return nums


def odd_even_sort(nums):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(1, len(nums)-1, 2):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                draw_nums_highlight(nums, i+1)
                sorted = False
        
        for j in range(0, len(nums)-1, 2):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                draw_nums_highlight(nums, j+1)
                sorted = False

    return nums


def main():
    nums = set_nums()
    sleep(PAUSE)

    nums = shuffle_nums(nums)
    sleep(PAUSE)

    screen.title("Bubble Sort")
    nums = bubble_sort(nums)
    draw_nums(nums)
    sleep(PAUSE)

    nums = shuffle_nums(nums)
    sleep(PAUSE)

    screen.title("Insertion Sort")
    nums = insertion_sort(nums)
    draw_nums(nums)
    sleep(PAUSE)

    nums = shuffle_nums(nums)
    sleep(PAUSE)

    screen.title("Shaker Sort")
    nums = shaker_sort(nums)
    draw_nums(nums)
    sleep(PAUSE)

    nums = shuffle_nums(nums)
    sleep(PAUSE)

    """screen.title("Merge Sort")
    nums = merge_sort(nums)
    draw_nums(nums)
    sleep(PAUSE)

    nums = shuffle_nums(nums)
    sleep(PAUSE)"""

    screen.title("Odd-Even Sort")
    nums = odd_even_sort(nums)
    draw_nums(nums)
    sleep(PAUSE)


if __name__ == "__main__":
    main()
    done()
