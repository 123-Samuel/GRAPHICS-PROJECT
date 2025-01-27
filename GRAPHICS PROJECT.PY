# name of student             Id number              Section
#1 Samuel Zenebe             ugr/31182/15            51
#2 Muse fikadu                 ugr/30980/15            51
#3 Hemen Girma               ugr/30650/15            51
#4 Eliyas Tiruneh              ugr/30458/15            51 
#5 Sitra Taha                    ugr/31243/15            51
#6 Gelila Mesfin               ugr/30583/15             51
from cs1graphics import *
paper=Canvas(1300,700,"Skyblue","world")
import time
import math

                            ### Grass ###
r = Rectangle(1300, 1000, Point(650,850))
r.setFillColor("green2")
paper.add(r)
                            ### House ###

g5p=Polygon(Point(155,465), Point(155,445),Point(180,445), Point(180,280),Point(140,280),Point(140,260),Point(250,190),Point(715,190),Point(825,260),Point(825,280),Point(785,280),Point(785,445),Point(805,445),Point(805,465),Point(755,465),Point(195,465))
def house():
    g5p=Polygon(Point(155,465), Point(155,445),Point(180,445), Point(180,280),Point(140,280),Point(140,260),Point(250,190),Point(715,190),Point(825,260),Point(825,280),Point(785,280),Point(785,445),Point(805,445),Point(805,465),Point(755,465),Point(195,465))
    g5p.setDepth(18)
    g5p.setFillColor("white")
    paper.add(g5p)
    
    door4 =  Rectangle(110, 130, Point(500,400))
    door4.setDepth(17)
    door4.setFillColor("brown")
    door4.setBorderWidth(3)
    paper.add(door4)
    z = Path(Point(500,335),Point(500,465))
    z.setDepth(17)
    z.setBorderWidth(3)
    paper.add(z)
    t = Circle(5, Point(500,400))
    t.setFillColor('black')
    t.setDepth(17)
    paper.add(t)
    g5r=Polygon(Point(140,280),Point(140,260),Point(250,190),Point(715,190),Point(825,260),Point(825,280))
    g5r.setFillColor('gray')
    g5r.setDepth(17)
    paper.add(g5r)
    
                                                   ###  road ###
    road=Polygon(Point(0,500),Point(1300,500),Point(1300,610),Point(0,610))
    road.setFillColor("darkgrey")
    paper.add(road)
    garden=Polygon(Point(0,550),Point(1300,550),Point(1300,560),Point(0,560))
    garden.setFillColor("green")
    paper.add(garden)

    pa=Path(Point(50,605),Point(200,605))
    p1=Path(Point(50,585),Point(200,585))
    p2=Path(Point(50,565),Point(200,565))
    p3=Path(Point(50,545),Point(200,545))

    p4=Path(Point(50,525),Point(200,525))
    p5=Path(Point(50,505),Point(200,505))
    pa.setBorderWidth(6)
    p1.setBorderWidth(6)
    p2.setBorderWidth(6)
    p3.setBorderWidth(6)
    p4.setBorderWidth(6)
    p5.setBorderWidth(6)
    pa.setBorderColor("white")
    p1.setBorderColor("white")
    p2.setBorderColor("white")
    p3.setBorderColor("white")
    p4.setBorderColor("white")
    p5.setBorderColor("white")
    paper.add(pa)
    paper.add(p1)
    paper.add(p2)
    paper.add(p3)
    paper.add(p4)
    paper.add(p5)

    bulb1=Path(Point(220,610),Point(220,530),Point(270,525))
    bulb2=Path(Point(420,610),Point(420,530),Point(470,525))
    bulb3=Path(Point(620,610),Point(620,530),Point(670,525))
    bulb4=Path(Point(820,610),Point(820,530),Point(870,525))
    bulb5=Path(Point(1020,610),Point(1020,530),Point(1070,525))
    bulb6=Path(Point(1240,610),Point(1240,530),Point(1270,525))
    bulb1.setBorderWidth(6)
    bulb2.setBorderWidth(6)
    bulb3.setBorderWidth(6)
    bulb4.setBorderWidth(6)
    bulb5.setBorderWidth(6)
    bulb6.setBorderWidth(6)
    bulb1.setBorderColor("white")
    bulb2.setBorderColor("white")
    bulb3.setBorderColor("white")
    bulb4.setBorderColor("white")
    bulb5.setBorderColor("white")
    bulb6.setBorderColor("white")
    paper.add(bulb1)
    bulb1.setDepth(5)
    bulb2.setDepth(5)
    bulb3.setDepth(5)
    bulb4.setDepth(5)
    bulb5.setDepth(5)
    bulb6.setDepth(5)
    paper.add(bulb2)
    paper.add(bulb3)
    paper.add(bulb4)
    paper.add(bulb5)
    paper.add(bulb6)
house()

t1 = Circle(7, Point(270,530))
t2 = Circle(7, Point(470,530))
t3 = Circle(7, Point(670,530))
t4 = Circle(7, Point(870,530))
t5 = Circle(7, Point(1070,530))
t6 = Circle(7, Point(1270,530))
t1.setDepth(4)
t2.setDepth(4)
t3.setDepth(4)
t4.setDepth(4)
t5.setDepth(4)
t6.setDepth(4)
t1.setFillColor('white')
t2.setFillColor('white')
t3.setFillColor('white')
t4.setFillColor('white')
t5.setFillColor('white')
t6.setFillColor('white')
paper.add(t1)
paper.add(t2)
paper.add(t3)
paper.add(t4)
paper.add(t5)
paper.add(t6)

w1 = Square(130,Point(300,360))
w1.setDepth(17)
w1.setFillColor('orange')
w1.setBorderWidth(3)

paper.add(w1)
w2=w1.clone()
w2.moveTo(680,360)
w2.setDepth(17)

paper.add(w2)
def draw_car():
    car = Layer()
    car = add_tires(car)
    car = add_tires2(car)
    car = add_body(car)
    car.moveTo(50,590)
    car.setDepth(10)
    paper.add(car)
    return car
def animate_car(car):
    for i in range(660):
       car.move(2,0)
def add_tires(car):
    tire1 = Circle(10, Point(-35,-10))
    tire1.setFillColor('black')
    car.add( tire1)
    b = Circle(5,Point(55,-30))
    b.setFillColor("white")
    car.add(b)
    b1 = Circle(5,Point(-55,-30))
    b1.setFillColor("white")
    car.add(b1)
    return car
def add_tires2(car):
    tire2 = Circle(10, Point(35,-10))
    tire2.setFillColor('black')
    car.add(tire2)
    return car
def add_body(car):
    body = Polygon(Point(-55,-10),Point(-55,-40),Point(-25,-40),Point(-25,-60),Point(25,-60),Point(25,-40),Point(55,-40),Point(55,-10))
    body.setFillColor('red')
    body.setDepth(60)
    car.add(body) 
    return car
def draw_and_move_car():
    a=draw_car()
    animate_car(a)
    a.moveTo(1300,530)
    for i in range(400):
       a.move(-2,0)
#draw_and_move_car()
                                    ###  sun ###
sun = Circle(30)
sun.setFillColor("yellow")
sun.setDepth(60)
paper.add(sun)
def animate_sunrise(sun):
     w = paper.getWidth()
     h = 350
     r = sun.getRadius()
     x0 = w / 2.0
     y0 = h + r
     max_x  = w / 2.0 - r
     max_y  = h
     for angle in range(721):
         rad = (angle/360.0) * math.pi
         x = x0 - max_x * math.cos(rad)
         y = y0 - max_y * math.sin(rad)
         
         sun.moveTo(x, y)
         time.sleep(0.03)
     moon = Circle(30)
     moon.setFillColor("gray")
     moon.setDepth(9)
     moon.moveTo(1200, 100)
     paper.add(moon)
def dark():
    paper.setBackgroundColor("black")
    t1.setFillColor('yellow')
    t2.setFillColor('yellow')
    t3.setFillColor('yellow')
    t4.setFillColor('yellow')
    t5.setFillColor('yellow')
    t6.setFillColor('yellow')
    r.setFillColor("blueviolet")
    w1.setFillColor('yellow')
    w2.setFillColor('yellow')
house()
draw_and_move_car()
animate_sunrise(sun)
dark()
