import turtle
import random
import time

# Game setup
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=900, height=700)
wn.tracer(0)  # Turns off screen updates

# Get player name
player_name = wn.textinput("Snake Game", "Enter your name:")
if not player_name:
    player_name = "Player"

# Game variables
score = 0
level = 1
max_level = 5
high_score = 0
game_over = False
game_won = False

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "right"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Obstacles
obstacles = []
for _ in range(level * 2):  # More obstacles at higher levels
    obstacle = turtle.Turtle()
    obstacle.speed(0)
    obstacle.shape("square")
    obstacle.color("dark blue")
    obstacle.penup()
    x = random.randint(-13, 10) * 20
    y = random.randint(-8, 7) * 20
    # Ensure obstacle doesn't spawn on borders or too close to center
    while (abs(x) < 100 and abs(y) < 60) or (x, y) == (0, 0) or (x, y) == (0, 100):
        x = random.randint(-13, 10) * 20
        y = random.randint(-8, 7) * 20
    obstacle.goto(x, y)
    obstacles.append(obstacle)

# Pen for score display
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 150)
pen.write(f"Player: {player_name}  Score: {score}  Level: {level}  High Score: {high_score}", 
          align="center", font=("Courier", 12, "normal"))

# Snake body segments
segments = []

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop
while True:
    wn.update()
    
    # Check for border collision
    if (head.xcor() > 290 or head.xcor() < -290 or 
        head.ycor() > 190 or head.ycor() < -190):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        
        # Hide segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear segments list
        segments.clear()
        
        # Reset score and level
        score = 0
        level = 1
        
        # Update score display
        pen.clear()
        pen.write(f"Player: {player_name}  Score: {score}  Level: {level}  High Score: {high_score}", 
                  align="center", font=("Courier", 12, "normal"))
        
        # Reset obstacles
        for obstacle in obstacles:
            obstacle.goto(1000, 1000)
        obstacles = []
        for _ in range(level * 2):
            obstacle = turtle.Turtle()
            obstacle.speed(0)
            obstacle.shape("square")
            obstacle.color("dark blue")
            obstacle.penup()
            x = random.randint(-13, 10) * 20
            y = random.randint(-8, 7) * 20
            while (abs(x) < 100 and abs(y) < 60) or (x, y) == (0, 0):
                x = random.randint(-13, 10) * 20
                y = random.randint(-8, 7) * 20
            obstacle.goto(x, y)
            obstacles.append(obstacle)
    
    # Check for food collision
    if head.distance(food) < 20:
        # Move food to random spot
        x = random.randint(-13, 10) * 20
        y = random.randint(-8, 7) * 20
        food.goto(x, y)
        
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)
        
        # Increase score
        score += 10
        
        if score > high_score:
            high_score = score
        
        # Level up every 3 foods
        if len(segments) % 3 == 0 and level < max_level:
            level += 1
            
            # Add more obstacles
            for _ in range(2):  # Add 2 more obstacles per level
                obstacle = turtle.Turtle()
                obstacle.speed(0)
                obstacle.shape("square")
                obstacle.color("dark blue")
                obstacle.penup()
                x = random.randint(-13, 10) * 20
                y = random.randint(-8, 7) * 20
                while (abs(x) < 100 and abs(y) < 60) or (x, y) == (0, 0):
                    x = random.randint(-13, 10) * 20
                    y = random.randint(-8, 7) * 20
                obstacle.goto(x, y)
                obstacles.append(obstacle)
        
        # Update score display
        pen.clear()
        pen.write(f"Player: {player_name}  Score: {score}  Level: {level}  High Score: {high_score}", 
                  align="center", font=("Courier", 12, "normal"))
    
    # Check for obstacle collision
    for obstacle in obstacles:
        if head.distance(obstacle) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            
            # Hide segments
            for segment in segments:
                segment.goto(1000, 1000)
            
            # Clear segments list
            segments.clear()
            
            # Reset score and level
            score = 0
            level = 1
            
            # Update score display
            pen.clear()
            pen.write(f"Player: {player_name}  Score: {score}  Level: {level}  High Score: {high_score}", 
                      align="center", font=("Courier", 12, "normal"))
            
            # Reset obstacles
            for obstacle in obstacles:
                obstacle.goto(1000, 1000)
            obstacles = []
            for _ in range(level * 2):
                obstacle = turtle.Turtle()
                obstacle.speed(0)
                obstacle.shape("square")
                obstacle.color("dark blue")
                obstacle.penup()
                x = random.randint(-13, 10) * 20
                y = random.randint(-8, 7) * 20
                while (abs(x) < 100 and abs(y) < 60) or (x, y) == (0, 0):
                    x = random.randint(-13, 10) * 20
                    y = random.randint(-8, 7) * 20
                obstacle.goto(x, y)
                obstacles.append(obstacle)
    
    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    
    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    
    move()
    
    # Check for head collision with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            
            # Hide segments
            for segment in segments:
                segment.goto(1000, 1000)
            
            # Clear segments list
            segments.clear()
            
            # Reset score and level
            score = 0
            level = 1
            
            # Update score display
            pen.clear()
            pen.write(f"Player: {player_name}  Score: {score}  Level: {level}  High Score: {high_score}", 
                      align="center", font=("Courier", 12, "normal"))
            
            # Reset obstacles
            for obstacle in obstacles:
                obstacle.goto(1000, 1000)
            obstacles = []
            for _ in range(level * 2):
                obstacle = turtle.Turtle()
                obstacle.speed(0)
                obstacle.shape("square")
                obstacle.color("yellow")
                obstacle.penup()
                x = random.randint(-13, 10) * 20
                y = random.randint(-8, 7) * 20
                while (abs(x) < 100 and abs(y) < 60) or (x, y) == (0, 0):
                    x = random.randint(-13, 10) * 20
                    y = random.randint(-8, 7) * 20
                obstacle.goto(x, y)
                obstacles.append(obstacle)
    
    # Check win condition
    if level == max_level and len(segments) >= 50:  # Approximate win condition
        pen.clear()
        pen.goto(0, 0)
        pen.write(f"Congratulations {player_name}!\nYou Won!\nFinal Score: {score}", 
                  align="center", font=("Courier", 24, "normal"))
        time.sleep(3)
        break
    
    time.sleep(0.1)
wn.mainloop()
