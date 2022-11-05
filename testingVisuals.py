# import pandas as pd 
# df = pd.DataFrame({ 
#     'Fname':['Harry','Sally','Paul','Abe','June','Mike','Tom'], 
#     'Age':[21,34,42,18,24,80,22], 
#     'Weight': [180, 130, 200, 140, 176, 142, 210], 
#     'Gender':['M','F','M','M','F','M','M'], 
#     'State':['Washington','Oregon','California','Washington','Nevada','Texas','Nevada'],
#     'Children':[4,1,2,3,0,2,0],
#     'Pets':[3,2,2,5,0,1,5] 
# }) 
# print (df) 


# TURTLE STAR
# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

# import package and making objects
from turtle import *
 
 
sc=Screen()
trtl=Turtle()
 
# method to draw y-axis lines
def drawy(val):
     
    # line
    trtl.forward(300)
     
    # set position
    trtl.up()
    trtl.setpos(val,300)
    trtl.down()
     
    # another line
    trtl.backward(300)
     
    # set position again
    trtl.up()
    trtl.setpos(val+10,0)
    trtl.down()
     
# method to draw y-axis lines
def drawx(val):
     
    # line
    trtl.forward(300)
     
    # set position
    trtl.up()
    trtl.setpos(300,val)
    trtl.down()
     
    # another line
    trtl.backward(300)
     
    # set position again
    trtl.up()
    trtl.setpos(0,val+10)
    trtl.down()
     
# method to label the graph grid
def lab():
     
    # set position
    trtl.penup()
    trtl.setpos(155,155)
    trtl.pendown()
     
    # write 0
    trtl.write(0,font=("Verdana", 12, "bold"))
     
    # set position again
    trtl.penup()
    trtl.setpos(290,155)
    trtl.pendown()
     
    # write x
    trtl.write("x",font=("Verdana", 12, "bold"))
     
    # set position again
    trtl.penup()
    trtl.setpos(155,290)
    trtl.pendown()
     
    # write y
    trtl.write("y",font=("Verdana", 12, "bold"))
     
 
# Main Section
# set screen
sc.setup(800,800)   
 
# set turtle features
trtl.speed(100)
trtl.left(90) 
trtl.color('lightgreen')
 
# y lines
for i in range(30):
    drawy(10*(i+1))
 
# set position for x lines
trtl.right(90)
trtl.up()
trtl.setpos(0,0)
trtl.down()
 
# x lines
for i in range(30):
    drawx(10*(i+1))
 
# axis
trtl.color('green')
 
# set position for x axis
trtl.up()
trtl.setpos(0,150)
trtl.down()
 
# x-axis
trtl.forward(300)
 
# set position for y axis
trtl.left(90)
trtl.up()
trtl.setpos(150,0)
trtl.down()
 
# y-axis
trtl.forward(300)
 
# labeling
lab()
 
# hide the turtle
trtl.hideturtle()
done()