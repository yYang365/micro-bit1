def on_logo_touched():
    if not (running):
        basic.pause(100)
        countLed()
        basic.pause(1000)
        showSaved()
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def on_button_pressed_a():
    global running
    running = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def countLed():
    global count
    count = 0
    for list2 in listX:
        for 值 in list2:
            if 值:
                count += 1
    basic.clear_screen()
    if count:
        basic.show_number(count)

def on_button_pressed_b():
    global running
    running = 0
    saveToList()
input.on_button_pressed(Button.B, on_button_pressed_b)

def saveToList():
    global listX, listY
    listX = []
    for x2 in range(5):
        listY = []
        for y2 in range(5):
            listY.append(led.point(x2, y2))
        listX.append(listY)
def showSaved():
    basic.clear_screen()
    for x in range(5):
        for y in range(5):
            if listX[x][y]:
                led.plot(x, y)
listY: List[bool] = []
listX: List[List[bool]] = []
count = 0
running = 0
basic.show_icon(IconNames.HEART)

def on_forever():
    if running:
        led.toggle(randint(0, 4), randint(0, 4))
basic.forever(on_forever)
