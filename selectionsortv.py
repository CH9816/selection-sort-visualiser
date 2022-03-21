import random as ran
import turtle as t


# rendering visualisation with turtle
def turtlerenderbars(a, focus = [], altfocus = [], altaltfocus= []):
    t.tracer(0,0),t.update(),t.bgcolor('black'),t.clear(),t.hideturtle()
    for i in range(len(a)):
        t.color('midnightblue')
        if a[i] in focus:
            t.pencolor('red')
        elif a[i] in altfocus:
            t.pencolor('white')
        elif a[i] in altaltfocus:
            t.pencolor('midnightblue')
        else:
            t.color('blue')
        t.penup(), t.goto((i*(800 / len(a)))-400, -380), t.pendown(), t.seth(90), t.pensize(500/len(a)), t.fd(a[i]*(700//max(a)))

def write(x,y,size,text):
    startpos = t.pos()

    t.penup()
    t.goto(x,y)
    t.pendown()

    t.write(text, font = ('Arial', size, 'normal'))

    t.penup()
    t.goto(startpos)
    t.pendown()
    

# used for colours, not actual sorting
# needs optimisation
def findall(item, array):
    toberet = []
    for i in array:
        if i == item:
            toberet.append(i)
    return toberet


# actually carry out the sorting
def selectionsort(array):
    # to count array reading and calculations, to test speed
    # because visual speed can depend on render speed rather than actual sorting speed
    accesscount = 0
    compcount = 0
    writecount = 0
    for focus in range(len(array)):
        accesscount += 1
        for index in range(len(array)):
            accesscount += 1
            if array[focus] < array[index]:
                compcount += 1
                array[index], array[focus] = array[focus], array[index]
                writecount += 1
                if not lowspec:
                    turtlerenderbars(array, [array[index],array[focus]] ,[array[x] for x in range(len(array)) if array[x] > array[index] and x < focus], [array[x] for x in range(len(array)) if x > focus])
                else:
                    turtlerenderbars(array, [array[index], array[focus]])
                    
                # showing access count and comparison count
                t.color('blue')
                write(-470, 380, 10, 'reads:')
                write(-470, 350, 10, 'comparisons:')
                write(-470, 320, 10, 'writes:')
                write(-380,370,20,accesscount)
                write(-380,340, 20, compcount)
                write(-380, 310, 20, writecount)
                
            else:
                compcount += 1
    




if __name__ == '__main__':

    # can be changed, up to 500
    listl = 80

    # to change if, when sorted, should the array be shuffled and sorted again
    repeat = True

    # can be made true to increase performance at the cost of some of the visuals
    lowspec = False
    
    # generating array
    array = [x for x in range(listl)]

    ran.shuffle(array)
    
    while True:
        selectionsort(array)
        if repeat:
            ran.shuffle(array)
