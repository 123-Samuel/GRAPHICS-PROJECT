# name of student             Id number              Section
#1 Samuel Zenebe             ugr/31182/15            51
#2 Muse fikadu                 ugr/30980/15            51
#3 Hemen Girma               ugr/30650/15            51
#4 Eliyas Tiruneh              ugr/30458/15            51 
#5 Sitra Taha                    ugr/31243/15            51
#6 Gelila Mesfin               ugr/30583/15             51
import time
from cs1graphics import *
from time import *
c=Canvas(1400,1000,"light blue","graphics project by muse")

buble = Layer()

# Create 5 circles for the cloud shape
circle1 = Circle(40, Point(-40, 0))
circle2 = Circle(40, Point(-20, -20))
circle3 = Circle(40, Point(0, 0))
circle4 = Circle(40, Point(20, -20))
circle5 = Circle(40, Point(40, 0))

# Set the fill color and border color of the circles to white
circle1.setFillColor('white')
circle1.setBorderColor('white')
circle2.setFillColor('white')
circle2.setBorderColor('white')
circle3.setFillColor('white')
circle3.setBorderColor('white')
circle4.setFillColor('white')
circle4.setBorderColor('white')
circle5.setFillColor('white')
circle5.setBorderColor('white')

# Add the circles to the cloud layer
buble.add(circle1)
buble.add(circle2)
buble.add(circle3)
buble.add(circle4)
buble.add(circle5)



idea=Layer()
buble.moveTo(600,380)
buble.scale(2)
buble2=buble.clone()
buble2.scale(0.25)
buble2.moveTo(370,500)
buble3=buble.clone()
buble3.scale(0.125)
buble3.moveTo(350,550)
buble.scale(1.5)

idea.add(buble)
idea.add(buble2)
idea.add(buble3)

content=Rectangle(310,220,Point(600,360))
content.setFillColor("white")
content.setBorderWidth(0)

# txt=Text("YOU HIT ME DUMB!!!", 50,Point(600,340))
# txt.setFontColor("black")
# txt.setDepth(49)
# idea.add(txt)
idea.add(content)
idea.scale(0.5)
idea.moveTo(100,200)


idea2=idea.clone()
idea2.scale(2)
#c.add(idea)


man=Layer()
head=Circle(20,Point(100,250))
head.setFillColor((245, 222, 179))
man.add(head)
body=Polygon(Point(75,290),Point(80,275),Point(130,275),Point(135,290),Point(130,330),Point(80,330))
body.setFillColor((38,252,245))
man.add(body)
neck=Path(Point(95,270),Point(95,275))
neck.setBorderColor("white")
man.add(neck)
neck1=Path(Point(105,270),Point(105,275))
neck1.setBorderColor("white")
man.add(neck1)
eye=Circle(5,Point(115,247))
man.add(eye)
eye2=Circle(5,Point(100,247))
man.add(eye2)
eye3=Circle(2,Point(115,247))
man.add(eye3)
eye3.setFillColor("black")
eye4=Circle(2,Point(100,247))
man.add(eye4)
eye4.setFillColor("black")
nouse=Path(Point(108,250),Point(108,255))
man.add(nouse)
mouse=Ellipse(5,3,Point(108,262))
man.add(mouse)
hand=Polygon(Point(80,275),Point(60,300),Point(60,305),Point(70,305),Point(77,305))
hand.setFillColor("skyblue")
man.add(hand)
hand2=Polygon(Point(130,275),Point(150,300),Point(150,305),Point(140,305),Point(133,305))
hand2.setFillColor("skyblue")
man.add(hand2)
leg=Rectangle(10,20,Point(115,340))
leg.setFillColor('skyblue')
man.add(leg)
leg=Rectangle(10,20,Point(90,340))
leg.setFillColor('skyblue')
man.add(leg)
# racket=Circle(15,Point(40,300))
# racket.setFillColor('red')
# man.add(racket)
rect=Rectangle(10,20,Point(70,314))
rect.setFillColor((245, 222, 179))
rect.setDepth(1)
rect1=Rectangle(10,20,Point(140,314))
rect1.setFillColor((245, 222, 179))
rect1.setDepth(1)
man.add(rect)
man.add(rect1)


def re(a,b,c,d,e,f):
    r=Rectangle(a,b,Point(c,d))
    f.add(r)
    r.setFillColor(e)
#funtion to draw triangle
def tri(f,g,h,i,j,k,l,m):
    t=Polygon(Point(f,g),Point(h,i),Point(j,k))
    m.add(t)
    t.setFillColor(l)

def pa(a,b,c,d,e,f,g):
    p=Path(Point(a,b),Point(c,d))
    p.setBorderColor(e)
    p .setBorderWidth(f)
    g.add(p)
def ci(x,y,z,w,u,v):
    c=Circle(x,Point(y,z))
    c.setFillColor(w)
    c.setBorderColor(v)
    u.add(c)
def p(x,y,z,a,b,c,d,e,f,g,h,i,j,k,m,n):
    po=Polygon(Point(x,y),Point(z,a),Point(b,c),Point(d,e),Point(h,i),Point(j,k),Point(m,n))
    f.add(po)
    po.setFillColor(g)
def pol(x,y,z,a,b,c,d,e,f,g):
    po=Polygon(Point(x,y),Point(z,a),Point(b,c),Point(d,e))
    f.add(po)
    po.setFillColor(g)

#adding the road
road=Layer()
re(1380,210,700,600,"black",road)
re(100,10,60,565,"white",road)
re(100,10,60,635,"white",road)
re(100,10,210,565,"white",road)
re(100,10,210,635,"white",road)
re(100,10,460,565,"white",road)
re(100,10,460,635,"white",road)
re(100,10,610,565,"white",road)
re(100,10,610,635,"white",road)
re(100,10,860,565,"white",road)
re(100,10,860,635,"white",road)
re(100,10,1010,565,"white",road)
re(100,10,1010,635,"white",road)
re(100,10,1260,565,"white",road)
re(100,10,1260,635,"white",road)
re(1400, 400, 700, 750,"green", c)
re(1400, 150, 700, 425,"green", c)
c.add(road)

#addin the cars
car=Layer()
p(100,550,200,550,200,500,220,500,car,"blue",250,530,250,580,100,580)
ci(15,118,580,"white",car,"white")
ci(15,232,580,"white",car,"white")
ra=Rectangle(100,60,Point(150,520))
ra.setFillColor("red")
ra.adjustReference(-150,300)
car.add(ra)
c.add(car)
car3=Layer()
caa=Polygon(Point(0,380),Point(-50,380),Point(-80,350),Point(-180,350),Point(-200,380),Point(-230,380),Point(-230,420),Point(0,420))
caa.setFillColor("purple")
car3.add(caa)
ci(15,-40,420,"black",car3,"white")
ci(15,-200,420,"black",car3,"white")
rec2=Rectangle(30,4,Point(-40,420))
rec2.setFillColor("white")
car3.add(rec2)
rec3=Rectangle(30,4,Point(-200,420))
rec3.setFillColor("white")
car3.add(rec3)
c.add(car3)
car3.moveTo(0,170)

#adding the buildings
pol(425, 420, 460, 380, 460, 80, 425, 120, c, "brown")
pol(425, 270, 575, 270, 610, 230, 460, 230, c, "brown")
re(150, 300, 350, 270,"brown", c)
re(50, 50, 310, 150,"yellow", c)
re(50, 50, 390, 150,"yellow", c)
re(50, 50, 310, 230,"yellow", c)
re(50, 50, 390, 230,"yellow", c)
re(50, 50, 310, 310,"yellow", c)
re(50, 50, 390, 310,"yellow", c)
re(60, 70, 390, 380,"gray", c)
re(60, 70, 310, 380,"gray", c)
re(55, 20, 390, 360,"yellow", c)
re(55, 20, 310, 360,"yellow", c)
re(150, 150, 500, 345,"brown", c)
re(150, 300, 650, 270,"brown", c)
re(50, 50, 610, 150,"yellow", c)
re(50, 50, 690, 150,"yellow", c)
re(50, 50, 610, 230,"yellow", c)
re(50, 50, 690, 230,"yellow", c)
re(50, 50, 610, 310,"yellow", c)
re(50, 50, 690, 310,"yellow", c)
re(60, 70, 690, 380,"gray", c)
re(60, 70, 610, 380,"gray", c)
re(55, 20, 690, 360,"yellow", c)
re(55, 20, 610, 360,"yellow", c)
re(50, 50, 460, 310,"yellow", c)
re(50, 50, 540, 310,"yellow", c)
re(60, 70, 460, 380,"gray", c)
re(60, 70, 540, 380,"gray", c)
re(55, 20, 540, 360,"yellow", c)
re(55, 20, 460, 360,"yellow", c)
pol(275, 120, 425, 120, 460, 80, 310, 80, c, "brown")
pol(575, 120, 725, 120, 760, 80, 610, 80, c, "brown")
re(150, 150, 1000, 345,"red", c)
pol(925, 270, 965, 240, 1115, 240, 1075, 270, c, "red")
pol(1075, 420, 1115, 380, 1115, 240, 1075, 270, c, "red")
re(60, 120, 960, 350,"yellow", c)
re(60, 60, 1030, 320,"yellow", c)
pol(725, 420, 760, 380, 760, 80, 725, 120, c, "brown")
re(10, 200, 150, 625,"gray", c)
ci(30, 800, 495,"white", c, "white")
ci(30, 150, 495,"white", c, "white")
re(10, 200, 800, 625,"gray", c)

#adding the trees
tree1=Layer()
tri(200,505,300,505,250,405,"darkgreen",tree1)
tri(210,455,290,455,250,355,"darkgreen",tree1)
tri(220,405,280,405,250,305,"darkgreen",tree1)
re(40,30,250,520,"brown",tree1)
c.add(tree1)
tree1.moveTo(200,200)
tree2=Layer()
tri(700,505,800,505,750,405,"darkgreen",tree2)
tri(710,455,790,455,750,355,"darkgreen",tree2)
tri(720,405,780,405,750,305,"darkgreen",tree2)
re(40,30,750,520,"brown",tree2)
c.add(tree2)
tree2.moveTo(300,200)
tree3=Layer()
tri(200,505,300,505,250,405,"darkgreen",tree3)
tri(210,455,290,455,250,355,"darkgreen",tree3)
tri(220,405,280,405,250,305,"darkgreen",tree3)
re(40,30,250,520,"brown",tree3)
c.add(tree3)
tree3.scale(0.75)
tree3.moveTo(30,70)
tree4=Layer()
tri(700,505,800,505,750,405,"darkgreen",tree4)
tri(710,455,790,455,750,355,"darkgreen",tree4)
tri(720,405,780,405,750,305,"darkgreen",tree4)
re(40,30,750,520,"brown",tree4)
c.add(tree4)
tree4.scale(0.75)
tree4.moveTo(80,70)
ci(30, 1300, 100,"white", c, "white")
for i in range(200):#change it to 4500
    car.move(1.5,0)
    car3.move(4,0)
    rec2.rotate(3)
    rec3.rotate(3)
idea.scale(0.6)
idea.moveTo(440,350)
c.add(idea)
txt=Text("YOU HIT"
         " ME DUMB!!!", 10,Point(620,450))
c.add(txt)
# txt.setFontColor("black")
# txt.setDepth(49)
# idea.add(txt)


man.setDepth(1)
man.scale(0.7)
man.moveTo(440,350)
c.add(man)




mann2=Layer()
head2=Circle(20,Point(100,250))
head2.setFillColor((245, 222, 179))
mann2.add(head2)
body2=Polygon(Point(75,290),Point(80,275),Point(130,275),Point(135,290),Point(130,330),Point(80,330))
body2.setFillColor("brown")
mann2.add(body2)
neck2=Path(Point(95,270),Point(95,275))
neck2.setBorderColor("white")
mann2.add(neck2)
neck12=Path(Point(105,270),Point(105,275))
neck12.setBorderColor("white")
mann2.add(neck12)
eye2=Circle(5,Point(115,247))
mann2.add(eye2)
eye22=Circle(5,Point(100,247))
mann2.add(eye22)
eye32=Circle(2,Point(115,247))
mann2.add(eye32)
eye32.setFillColor("black")
eye42=Circle(2,Point(100,247))
mann2.add(eye42)
eye42.setFillColor("black")
nouse2=Path(Point(108,250),Point(108,255))
mann2.add(nouse2)
mouse2=Ellipse(5,3,Point(108,262))
mann2.add(mouse2)
hand2=Polygon(Point(80,275),Point(60,300),Point(60,305),Point(70,305),Point(77,305))
hand2.setFillColor("skyblue")
mann2.add(hand2)
hand22=Polygon(Point(130,275),Point(150,300),Point(150,305),Point(140,305),Point(133,305))
hand22.setFillColor("skyblue")
mann2.add(hand22)
leg2=Rectangle(10,20,Point(115,340))
leg2.setFillColor('black')
mann2.add(leg2)
leg2=Rectangle(10,20,Point(90,340))
leg2.setFillColor('black')
mann2.add(leg2)
# racket=Circle(15,Point(40,300))
# racket.setFillColor('red')
# man.add(racket)
rect2=Rectangle(10,20,Point(70,314))
rect2.setFillColor((245, 222, 179))
rect2.setDepth(1)
rect12=Rectangle(10,20,Point(140,314))
rect12.setFillColor((245, 222, 179))
rect12.setDepth(1)
mann2.add(rect2)
mann2.add(rect12)
c.add(mann2)

mann2.setDepth(1)
mann2.scale(0.7)
mann2.moveTo(650,350)



sleep(3)
c.remove(txt)
c.remove(idea)

idea.moveTo(630,350)
c.add(idea)

txt2=Text("SORRY I WASN'T FOCUSING ", 10 ,Point(820,450))
c.add(txt2)
sleep(3)

c.remove(txt2)
sleep(1)

txt3=Text("WHAT CAN I DO TO MAKE",10,Point(820,450))
txt4=Text("THINGS RIGHT",10,Point(820,470))
c.add(txt3)
c.add(txt4)

sleep(3)

c.remove(txt3)
c.remove(txt4)
c.remove(idea)


idea.moveTo(440,350)
c.add(idea)

txt5=Text("OH DIDN'T EXPECT THAT",10,Point(620,450))
txt6=Text("THOUGHT YOU WOULD",10,Point(620,450))
txt7=Text("RAGE AND TRY TO ESCAPE",10,Point(620,450))
txt8=Text("GUESS YOUR NICE PERSON",10,Point(620,450))

c.add(txt5)
sleep(3)
c.remove(txt5)

c.add(txt6)
sleep(3)
c.remove(txt6)

c.add(txt7)
sleep(3)
c.remove(txt7)

c.add(txt8)
sleep(3)
c.remove(txt8)

c.remove(idea)

idea.moveTo(630,350)
c.add(idea)
txt9=Text("SEND ME YOUR "
          "INSURANCE DETAIL",10,Point(820,470))
txt10=Text("I WILL MAKE SURE YOUR CAR IS",10,Point(820,470))
txt11=Text("FIXED AND YOU ALSO "
           "COMPENSATED",10,Point(820,470))
txt12=Text("SHALL WE GET A COFFE ",10,Point(820,470))

c.add(txt9)
sleep(3)
c.remove(txt9)

c.add(txt10)
sleep(3)
c.remove(txt10)

c.add(txt11)
sleep(3)
c.remove(txt11)

c.add(txt12)
sleep(3)
c.remove(txt12)
c.remove(idea)

idea.moveTo(440,350)
c.add(idea)

txt13=Text("SURE BUT FIRST LET",10,Point(620,450))
txt14=Text("US GET MY CAR TOWED",10,Point(620,450))
txt15=Text("AND THEN YOU WILL",10,Point(620,450))
txt16=Text("GIVE ME A LIFT",10,Point(620,450))

c.add(txt13)
sleep(3)
c.remove(txt13)
c.add(txt14)
sleep(3)
c.remove(txt14)
c.add(txt15)
sleep(3)
c.remove(txt15)
c.add(txt16)
sleep(3)
c.remove(txt16)
c.remove(idea)

c.remove(car)


for i in range(100):
    mann2.move(-1.8,0)
    # man.move(0,-1)
man.move(-5,0)

for i in range(100):
    man.move(0,-1)
    mann2.move(0,-1)
for i in range(200):
    man.move(2.1, 0)
    mann2.move(2.1, 0)
for i in range(100):
    man.move(0, -1)
    mann2.move(0, -1)

c.remove(man)
c.remove(mann2)

sleep(5)

c.add(man)
c.add(mann2)
for i in range(100):
    man.move(0, 1)
    mann2.move(0, 1)
for i in range(200):
    man.move(-2.1, 0)
    mann2.move(-2.1, 0)
for i in range(100):
    man.move(0,1)
    mann2.move(0,1)
for i in range(100):
    mann2.move(1.8,0)
    man.move(1.8,0)
c.remove(man)
c.remove(mann2)

for i in range(2000):
    car3.move(0.4,0)
    rec2.rotate(3)
    rec3.rotate(3)



group=Layer()
hh=Rectangle(600,400,Point(400,1400))
hh.setFillColor("purple")
hh.setBorderColor("blue")
hh.setBorderWidth(2)
group.add(hh)
gr=Text('GROUP4',16,Point(350,1250))
gr.setFontColor("white")
group.add(gr)
gr2=Text('GROUP MEMBERS',16,Point(350,1270))
gr2.setFontColor("white")
group.add(gr2)
gr3=Text('No ----- --- NAME     --------          ----------------       ID No',15,
         Point(350,1290))
gr3.setFontColor("white")
group.add(gr3)
c.add(group)
muk=Text('1  Muse Fikadu                          UGR/30980/15 ',18,
         Point(350,1315))
muk.setFontColor("white")
group.add(muk)
mub=Text('2  Sitra Taha                         UGR/31243/15 ',18,
         Point(350,1335))
mub.setFontColor("white")
group.add(mub)
mud=Text('3  Samuel Zenebe                           UGR/31182/15',18,
         Point(350,1355))
mud.setFontColor("white")
group.add(mud)
mul=Text('4  Eliayas Terhuneh                           UGR/30458/15 ',18,
         Point(350,1375))
mul.setFontColor("white")
group.add(mul)
mut=Text('5  Gelila Mesfen                           UGR/30583/15 ',18,
         Point(350,1395))
mut.setFontColor("white")

mut1=Text('6  Hemen Girma                            UGR/30650/15 ',18,
         Point(350,1415))
mut1.setFontColor("white")
group.add(mut1)
group.add(mut)
group.setDepth(1)
for i in range(1100):
     group.move(0,-1)
