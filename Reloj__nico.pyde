y = 0

def setup() :
    size(300, 600)

def draw() :
    global y
    background(175)



    ellipse(width/ 2, y, 50, 50)
    fill(19, 28, 237)
    if y > height :
        y = 0
    else:
        y = map(second(), 0, 59, 0, height)



    ellipse(width/ 2, y, 50, 50)
    fill(17, 242, 26)
    if y > height :
        y = 0
    else:
        y = map(minute(), 0, 59, 0, height)



    ellipse(width/ 2, y, 50, 50)
    fill(242, 17, 36)
    if y > height :
        y = 0
    else:
        y = map(hour(), 0, 24, 0, height)
