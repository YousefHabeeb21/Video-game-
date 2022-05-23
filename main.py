######################################################
# Project: <Video game>
# UIN: <652622525>
# repl.it URL: <https://replit.com/@CS111-Fall2021/Project-2-YousefHabeeb1#main.py>

# For this project, I received help from the following members of CS111.
# Imran Khan, netID 654046372: help with start and end screen 
# Waqar Ahmed, netID 662844795: help with dictionary and some collisions
 
######################################################
import turtle
import random



t1 = turtle.Turtle()
t1.ht()
t2 = turtle.Turtle()
t2.ht()
t3 = turtle.Turtle()
t3.ht()
t4 = turtle.Turtle()
t4.ht()

s = turtle.Screen()
s.setup(320, 320)
s.screensize(300,300)
s.tracer(0)
s.bgcolor("black")
s.bgpic("background.gif")

w,h = s.screensize()

speed_player = .1
level_number = 1
life_number = 3
score_player = 0
game_state = "over"


  # list of dictionaries for Game Objects
game_objects = [{"t": turtle.Turtle(), 'x': 0, 'y':125, 'radius':16, 'image':'warp_pipe.gif', 'type': 'objective'},{"t": turtle.Turtle(), 'x': 120, 'y':75, 'radius':16, 'image':'monster.gif', 'type': 'a'},{"t": turtle.Turtle(), 'x': -50, 'y':25, 'radius':16, 'image':'monster.gif', 'type': 's'},{"t": turtle.Turtle(), 'x': -70, 'y':-25, 'radius':16, 'image':'monster.gif', 'type': 'd'},{"t": turtle.Turtle(), 'x': -140, 'y':-75, 'radius':16, 'image':'monster.gif', 'type': 'f'},{"t": turtle.Turtle(), 'x': 0, 'y':-125, 'radius':16, 'image':'slime.gif', 'type': 'slime'}]
 
  
def animation():
  #score, level, and lives location
  global life_number
  global score_player
  game_state = "play"
  t4.clear()
  if game_state == "play":
    t2.pu()
    t2.goto(-150,130)
    t2.color('White')
    t2.pd()
    t2.clear()
    t2.write(f'Level:{1}', align = 'left')

    t3.pu()
    t3.goto(120,130)
    t3.color('White')
    t3.pd()
    t3.clear()
    t3.write(f'Lives:{life_number}', align = 'center')

    t1.pu()
    t1.goto(-150,-140)
    t1.color('White')
    t1.pd()
    t1.clear()
    t1.write(f'Score:{0}', align = 'left')

  while game_state == 'play' and life_number > 0:
    
    global level_number
    global speed_player
    for obj in game_objects:
      obj["t"].clear()


    #direction for monster
    for obj in game_objects:
      if (obj['type'] == 'a'):
        obj['x']+= speed_player
      elif (obj['type'] == 's'):
        obj['x']-= speed_player
      elif (obj['type'] == 'd'):
        obj['x']+= speed_player
      elif (obj['type'] == 'f'):
        obj['x']-= speed_player


    # monster loop
    for obj in game_objects:
      if obj['type']=='a' and obj['x']> 150 + obj['radius']:
        obj['x']= -w/2
      if obj['type']=='s' and obj['x']< -150 - obj['radius']:
        obj['x']= w/2
      if obj['type']=='d' and obj['x']> 150 + obj['radius']:
        obj['x']= -w/2
      if obj['type']=='f' and obj['x']< -150 - obj['radius']:
        obj['x']= w/2
      if obj['type']=='slime' and obj['x']> 150 + obj['radius']:
        obj['x']= 150
      if obj['type']=='slime' and obj['x']> 150 + obj['radius']:
        obj['x']= -150
      if obj['type']=='slime' and obj['x']> 150 + obj['radius']:
        obj['x']= -150
      if obj['type']=='slime' and obj['x']> 150 + obj['radius']:
        obj['x']= 150

    for obj in game_objects:
      x = obj['x']
      y = obj['y']
      t = obj['t']
      t.goto(x,y)


    #collision conditions
    for obj in game_objects:
      if game_objects[0]['t'].distance(game_objects[5]['t']) <= game_objects[3]['radius'] + game_objects[4]['radius']:
        game_objects[5]['t'].goto(0,-125)
        game_objects[5]['x'] = 0
        game_objects[5]['y'] = -125
        game_objects[0]['x'] =random.randint(-150,150)       
        score_player += 100
        t1.penup()
        t1.goto(-150,- 140)
        t1.color("white")
        t1.pendown()
        t1.clear()
        t1.write(f'Score:{score_player}', align = 'left')
        level_number += 1
        t2.penup()
        t2.goto(-150,130)
        t2.color("white")
        t2.pendown()
        t2.clear()
        t2.write(f'Level:{level_number}', align = 'left')
        speed_player += 0.025
      if game_objects[1]['t'].distance(game_objects[5]['t']) <= game_objects[1]['radius'] + game_objects[4]['radius']:
        game_objects[5]['t'].goto(0,-125)
        game_objects[5]['x'] = 0
        game_objects[5]['y'] = -125
        life_number -= 1
        t3.penup()
        t3.goto(120,130)
        t3.color("white")
        t3.pendown()
        t3.clear()
        t3.write(f'Lives:{life_number}',align = 'center')
      if game_objects[2]['t'].distance(game_objects[5]['t']) <= game_objects[1]['radius'] + game_objects[4]['radius']:
        game_objects[5]['t'].goto(0,-125)
        game_objects[5]['x'] = 0
        game_objects[5]['y'] = -125
        life_number -= 1
        t3.penup()
        t3.goto(120,130)
        t3.color("white")
        t3.pendown()
        t3.clear()
        t3.write(f'Lives:{life_number}', align = 'center')
      if game_objects[3]['t'].distance(game_objects[5]['t']) <= game_objects[2]['radius'] + game_objects[4]['radius']:
        game_objects[5]['t'].goto(0,-125)
        game_objects[5]['x'] = 0
        game_objects[5]['y'] = -125
        life_number -= 1
        t3.penup()
        t3.goto(120,130)
        t3.color("white")
        t3.pendown()
        t3.clear()
        t3.write(f'Lives:{life_number}', align = 'center')
      if game_objects[4]['t'].distance(game_objects[5]['t']) <= game_objects[3]['radius'] + game_objects[4]['radius']:
        game_objects[5]['t'].goto(0,-125)
        game_objects[5]['x'] = 0
        game_objects[5]['y'] = -125
        life_number -= 1
        t3.penup()
        t3.goto(120,130)
        t3.color("white")
        t3.pendown()
        t3.clear()
        t3.write(f'Lives:{life_number}', align = 'center')
    s.update()

#end screen
  if life_number == 0:
    s.clear()
    t1.color("red")
    t1.pu()
    t1.goto(0,30)
    t1.pd()
    t1.clear()
    t1.write(f'You Lost!', align = 'center')
    t1.pu()
    t1.goto(0,0)
    t1.pd()
    t1.write(f'Score:{score_player}', align = 'center')
    
def main():
  # how far the the left and right key pushes
  def left():
    obj['x'] -=50
  def up():
    obj['y'] +=50
  def right():
    obj['x'] +=50
  def down():
    obj['y'] -=50
  

  #gifs
  for obj in game_objects:
    s.addshape(obj["image"])
    obj["t"].shape(obj["image"])


#key funtion assignment
  for obj in game_objects:   
    if obj["type"]== "slime":
      s.listen()
      s.onkey(animation, "space")
      s.onkey(left,'Left')
      s.onkey(right,'Right')
      s.onkey(down,'Down')
      s.onkey(up,'Up')


#start screen
  if game_state == "over":
     
    t4.penup()
    t4.goto(0,-50)
    t4.pd()
    t4.write("Press space bar to play", font = 40, align="center")
    t4.pu()
    t4.goto(0,10)
    t4.color("black")
    t4.pd()
    t4.write("Slime Jumper", font= 60, align = "center")

main()





