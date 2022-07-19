import random
from turtle import Turtle, Screen, tracer, update, done, colormode
from time import sleep

NUMBER_OF_ELEMENTS = 30 # length of array that will be sorted
WIDTH = 600
WIDTH -= WIDTH % NUMBER_OF_ELEMENTS # make width proportional
HEIGHT = WIDTH
SCALE = int(WIDTH/NUMBER_OF_ELEMENTS)
DELAY = 0.01 # delay between each canvas update 
PAUSE = 0.5 # delay between shuffles and starting a new sort
SHUFFLES = 2 # how many times in multiples of array length the array is shuffle in between sorts
HIGHLIGHT_COLOR = (0,255,0) # color of highlighted bar when sorting

tracer(0,0)
colormode(255)


screen = Screen()
screen.bgcolor("white")
screen.title("Sorting Demo")
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

    return nums


def get_color(nums, i):
    return (int(50 + nums[i]/NUMBER_OF_ELEMENTS*100),
            int(50 + nums[i]/NUMBER_OF_ELEMENTS*175),
            int(100 + nums[i]/NUMBER_OF_ELEMENTS*150)
    )


def draw_nums(nums):
    t.clear()
    for i in range(len(nums)):
        t.setpos(SCALE*i - WIDTH/2, -HEIGHT/2)
        t.color(get_color(nums, i))
        t.pendown()
        t.forward(nums[i]*SCALE)
        t.penup()

    sleep(DELAY)
    update()


def draw_nums_highlight(nums, highlight):
    t.clear()
    for i in range(len(nums)):
        t.setpos(SCALE*i - WIDTH/2, -HEIGHT/2)
        t.color(get_color(nums, i))
        if i == highlight:
            t.color(HIGHLIGHT_COLOR)
        t.pendown()
        t.forward(nums[i]*SCALE)
        t.penup()

    sleep(DELAY)
    update()


def shuffle_nums(nums):
    screen.title("Shuffling...")
    for i in range(len(nums)*SHUFFLES):
        i = random.randint(0, NUMBER_OF_ELEMENTS-1)
        j = random.randint(0, NUMBER_OF_ELEMENTS-1)
        nums[i], nums[j] = nums[j], nums[i]
        draw_nums(nums)


def bubble(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                draw_nums_highlight(nums, j+1)


def insertion(nums):
    for i in range(1, len(nums)):
        key_item = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key_item:
            nums[j + 1] = nums[j]
            draw_nums_highlight(nums, j+1)
            j -= 1
        nums[j + 1] = key_item
        draw_nums_highlight(nums, j+1)


def shaker(nums):
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


def odd_even(nums):
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


def main():
    sorts = [bubble, insertion, shaker, odd_even]

    nums = set_nums()
    draw_nums(nums)
    sleep(2*PAUSE)

    for sort in sorts:
        shuffle_nums(nums)
        sleep(PAUSE)
        screen.title("Sort: " + sort.__name__)
        sort(nums)
        draw_nums(nums)
        sleep(PAUSE)
    
    screen.title("Sort Demo (finished)")


if __name__ == "__main__":
    main()
    done()
