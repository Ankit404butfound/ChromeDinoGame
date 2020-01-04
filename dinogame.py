import turtle
import time
import keyboard
import random
import mouse

count = 0
dx = 1
pdy = 1.8
mdy = -1.6
randcounter = 0
cloudx = 0.1
score = 0
distance = 25

img = r"C:\Users\pc\Desktop\dino\dinoo1.1.gif"
img1 = r"C:\Users\pc\Desktop\dino\dino1.1.gif"
img2 = r"C:\Users\pc\Desktop\dino\dino2.1.gif"
obj1 = r"C:\Users\pc\Desktop\dino\obs1.1.gif"
bgpic = r"C:\Users\pc\Desktop\dino\bgpic.png"
awrodh = r"C:\Users\pc\Desktop\dino\awrodh.gif"
binduimg = r"C:\Users\pc\Desktop\dino\dust.gif"
cloudimg = r"C:\Users\pc\Desktop\dino\cloud.gif"
obj2 = r"C:\Users\pc\Desktop\dino\obs2.1.gif"
obj3 = r"C:\Users\pc\Desktop\dino\obs3.1.gif"
obj4 = r"C:\Users\pc\Desktop\dino\obs4.1.gif"
obj5 = r"C:\Users\pc\Desktop\dino\obs5.1.gif"

imglst = [img1,img2]
objimg = [obj1,obj2,obj3,obj4,obj5]
elements = [img,img1,img2,awrodh,binduimg,cloudimg,obj1,obj2,obj3,obj4,obj5]

win = turtle.Screen()
for element in elements:
   win.addshape(element)
win.bgpic(bgpic)
##win.addshape(img)
##win.addshape(img1)
##win.addshape(img2)
##win.addshape(obj1)
##win.addshape(awrodh)
##win.addshape(binduimg)
##win.addshape(cloudimg)
##win.addshape(obj2)

win.tracer(0)

pen = turtle.Turtle()
pen.ht()
pen.color("grey")
pen.pu()
pen.goto(175,231)

dust2 = turtle.Turtle()
dust2.shape(awrodh)
dust2.pu()
dust2.ht()
dust2.goto(420,127)

dust = turtle.Turtle()
dust.shape(awrodh)
dust.pu()
dust.ht()
dust.goto(420,127)

dust3 = turtle.Turtle()
dust3.shape(awrodh)
dust3.pu()
dust3.ht()
dust3.goto(420,127)

obs1 = turtle.Turtle()
obs1.shape(obj1)
obs1.ht()
obs1.pu()
obs1.goto(420,140)

obs2 = turtle.Turtle()
obs2.shape(obj2)
obs2.ht()
obs2.pu()
obs2.goto(700,140)

cloud1 = turtle.Turtle()
cloud1.shape(cloudimg)
cloud1.ht()
cloud1.pu()
cloud1.goto(250,220)

cloud2 = turtle.Turtle()
cloud2.shape(cloudimg)
cloud2.ht()
cloud2.pu()
cloud2.goto(250,220)

dino = turtle
dino.lt(90)
dino.shape(img)
dino.pu()
dino.goto(-255,142)
dino.speed(10)

win.update()

def jump():
   global dy
   ycor = dino.ycor()
   if ycor > 142:
      dino.sety(ycor+dy)
      
   if ycor > 250:
      dy = mdy

   else:
      pass

def cloud1move():
   cloud1x = cloud1.xcor()
   cloud1.setx(cloud1x-cloudx)
   if cloud1x < 300:
      cloud1.st()
   if cloud1x < -300:
      cloud1x = random.randint(350,430)
      cloud1.ht()
      cloud1.setx(cloud1x)

def cloud2move():
   cloud2x = cloud2.xcor()
   cloud2.setx(cloud2x-cloudx)
   if cloud2x < 300:
      cloud2.st()
   if cloud2x < -300:
      cloud2x = random.randint(350,430)
      cloud2.ht()
      cloud2.setx(cloud2x)

def dustmove():
   dustx = dust.xcor()
   dust.setx(dustx-dx)
   if dustx < 300:
      dust.st()
   if dustx < -300:
      dustrx = random.randint(350,430)
      if dust.distance(dust2)<=50:
         dustrx = dustrx+200
      dust.ht()
      dust.setx(dustrx)

def dust2move():
   global dust2rx
   dust2x = dust2.xcor()
   dust2.setx(dust2x-dx)
   if dust2x < 300:
      dust2.st()
   if dust2x < -300:
      dust2rx = random.randint(350,430)
      dust2.ht()
      dust2.setx(dust2rx)

def dust3move():
   dust3x = dust3.xcor()
   dust3.setx(dust3x-dx)
   if dust3x < 300:
      dust3.st()
   if dust3x < -300:
      dust3rx = random.randint(350,430)
      dust3.ht()
      dust3.setx(dust3rx)

def obs1move():
   global distance
   obs1x = obs1.xcor()
   obs1.setx(obs1x-dx)
   if obs1x < 300:
     obs1.st()
   if obs1x < -300:
     obs1.ht()
     bgmg = random.choice(objimg)
     if bgmg == obj5:
        if obs1x <= -299:
           distance = 50
        else:
            distance = 25
     obs1.shape(bgmg)
     obs1rx = random.randint(350,430)
     if obs1.distance(obs2)<=200:
        obs1rx = obs1rx+200
     obs1.setx(obs1rx)

def obs2move():
   global distance
   obs2x = obs2.xcor()
   obs2.setx(obs2x-dx)
   if obs2x < 300:
     obs2.st()
   if obs2x < -300:
     obs2.ht()
     bgmg = random.choice(objimg)
     if bgmg == obj5:
        if obs2x <= -299:
           distance = 50
        else:
            distance = 25
     obs2.shape(bgmg)
     obs2rx = random.randint(350,430)
     if obs2.distance(obs1)<=200:
        obs2rx = obs2rx+200
     obs2.setx(obs2rx)


    
while True:
   win.update()
   randcounter = randcounter+1
   if randcounter % 50 == 0:
      count = count+1

   if randcounter % 50 == 0:
      score = score+1

   if randcounter % 500 == 0:
      dx = dx+0.1
      
   if count > 1:
     count = 0
     
   img = imglst[count]
   dino.shape(img)
   
   if keyboard.is_pressed("up") or keyboard.is_pressed("space"):
      if dino.ycor() <= 142.1:
         dy = pdy
         dino.sety(142.1)
         
      else:
         pass
   if dino.distance(obs1) <= distance or dino.distance(obs2) <= distance:
      pen.goto(-30,170)
      pen.write("Game over",align="left", font=("Comic Sans MS", 12, "bold"))
      while True:
         if keyboard.is_pressed("up") or keyboard.is_pressed("space"):
            count = 0
            dx = 1
            pdy = 1.8
            mdy = -1.6
            randcounter = 0
            cloudx = 0.1
            score = 0
            distance = 25
            dino.goto(-255,142)
            obs2.goto(900,140)
            obs1.goto(420,140)
            obs1.shape(obj1)
            obs2.shape(obj2)
            cloud2.goto(250,220)
            cloud1.goto(250,220)
            dust3.goto(420,127)
            dust.goto(420,127)
            dust2.goto(420,127)
            obs1.ht()
            obs2.ht()
            cloud2.ht()
            cloud1.ht()
            dust.ht()
            dust2.ht()
            dust3.ht()
            pen.goto(175,231)
            
            pen.clear()
            break
         if mouse.is_pressed():
            turtle.bye()
         else:
            pass


   pen.clear()
   pen.write(str(score), align="left", font=("Comic Sans MS", 12, "bold")) 
   
   jump()
   obs1move()
   dustmove()
   dust2move()
   dust3move()
   cloud1move()
   cloud2move()
   obs2move()
