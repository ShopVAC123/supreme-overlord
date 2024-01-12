import turtle

class PackGrid:
    def __init__(self):
        self.t = turtle.Turtle()
        self.dot_positions = []

    def create_maze(self, board):
        screen = turtle.Screen()
        screen.bgcolor("black")
        self.t = turtle.Turtle()
        self.t.speed(0) # Set the turtle speed to 0
        x, y = -200, 180
        width, height = 20, 20
        for row in board:
            for item in row:
                if item == 1: # Draw wall
                    self.draw_wall(self.t, x, y, width, height)
                elif item == 0:
                    radius = 0.2
                    self.draw_dot(self.t, x, y, radius)
                    self.dot_positions.append((x + radius, y + radius)) # Keep track of dot positions
                x += 21
            y -= 21
            x = -160
        screen.update()

    def draw_wall(self, t, x, y, width, height):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.pencolor("Teal")
        #t.begin_fill()
        for _ in range(4):
            t.forward(width)
            t.right(90)
        #t.end_fill()

    def draw_dot(self, t, x, y, radius):
        t.penup()
        t.goto(x + radius + 10, y + radius - 11) # Shift the dot's position by the radius
        t.pendown()
        t.color("white")
        t.begin_fill()
        t.circle(radius)
        t.end_fill()

    def check_pacman_position(self, pacman_x, pacman_y):
      for x, y in self.dot_positions:
          if abs(x - pacman_x) < 1 and abs(y - pacman_y) < 1: # If pacman's position matches a dot's position
              self.hide_dot(x, y) # Hide the dot
              return True

    def hide_dot(self, x, y):
      t = turtle.Turtle()
      t.penup()
      t.goto(x, y)
      t.pendown()
      t.color("black") # Change the dot's color to black
      t.begin_fill()
      t.circle(0.2)
      t.end_fill()
