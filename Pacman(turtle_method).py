import turtle
import random
import packGrid
import mailSEED

# Create a packGrid Instance
packGrid = packGrid.PackGrid()

# Sreen title
turtle.title("Pacman by Tyler Reed")
# Define the Board
board = [
  [3, 3, 3,	3, 3,	3, 3,	3, 3,	3, 3,	3, 3,	3, 3],
  [1, 1, 1,	1, 1, 1, 1,	1, 1,	1, 1,	1, 1,	1, 1],	
  [1, 0, 0,	0, 0,	0, 0,	1, 0,	0, 0,	0, 0,	0, 1],
  [1, 0, 1,	1, 0,	1, 0,	1, 0,	1, 0,	1, 1,	0, 1],
  [1, 0, 1,	1, 0,	1, 0,	1, 0,	1, 0,	1, 1,	0, 1],
  [1, 0, 0,	0, 0,	1, 0,	1, 0,	1, 0,	0, 0,	0, 1],
  [1, 1, 1,	0, 1,	1, 0,	1, 0,	1, 1,	0, 1,	1, 1],
  [0, 0, 0,	0, 0,	0, 0,	0, 0,	0, 0,	0, 0,	0, 0],
  [1, 1, 1,	0, 1,	1, 1,	1, 1,	1, 1,	0, 1,	1, 1],
  [1, 1, 1,	0, 1,	1, 1,	1, 1,	1, 1,	0, 1,	1, 1],
  [1, 1, 1,	0, 1,	0, 0,	0, 0,	0, 1,	0, 1,	1, 1],
  [1, 1, 1,	0, 0,	0, 1,	1, 1,	0, 0,	0, 1,	1, 1],
  [1, 0, 0,	0, 1,	0, 0,	1, 0,	0, 1,	0, 0,	0, 1],
  [1, 0, 1,	1, 1,	1, 0,	0, 0,	1, 1,	1, 1,	0, 1],
  [1, 0, 0,	0, 0,	0, 0,	1, 0,	0, 0,	0, 0,	0, 1],
  [1, 1, 1,	1, 1,	1, 1,	1, 1,	1, 1,	1, 1,	1, 1]
]
packGrid.create_maze(board)

# Draw the Pacman Character
def create_pacman():
    pacman = turtle.Turtle()
    # pacman.speed(2)
    pacman.pensize(2)
    pacman.shape("circle")
    pacman.shapesize(0.8, 0.8, 1)
    pacman.color("yellow")
    pacman.penup()
    pacman.goto(-3 , 23)
    return pacman

pacman = create_pacman()

# Move the pacman character
# def check_wall(x, y):
#   if board[x][y] == 1:
#     return True
#   return False

x = pacman.xcor()
y = pacman.ycor()

def move_up():
  global x, y
  new_x, new_y = x, y + 21
  if board[new_x][new_y] != 1:
      pacman.setheading(90)
      pacman.forward(21)
      x, y = new_x, new_y
  else:
      print("Can't move up!")
def move_down():
  pacman.setheading(270)
  pacman.forward(21)
def move_right():
  pacman.setheading(0)
  pacman.forward(21)
def move_left():
  pacman.setheading(180)
  pacman.forward(21)

  # if not check_wall(next_x, next_y):
  #     character.goto(next_x, next_y)
  #     character.xcor, character.ycor = next_x, next_y # Manually update the xcor and ycor attributes

# Game Logic
screen = turtle.Screen()
def game_logic():
  screen.listen()
  screen.onkey(move_up, "Up")
  screen.onkey(move_down, "Down")
  screen.onkey(move_left, "Left")
  screen.onkey(move_right, "Right")

def quit():
  screen.listen()
  if screen.onkey == "q":
    return True
    
score = 0
pacman_x, pacman_y = pacman.pos() # Get the position of Pac-Man
packGrid.check_pacman_position(pacman_x, pacman_y)
def main():
  game_logic()
  screen.mainloop()

while __name__ == "__main__":
  main()
  if packGrid.check_pacman_position(pacman_x, pacman_y) is True:
    score += 1
  if quit() is True:
    break
  else:
    print("Score: ", score)
