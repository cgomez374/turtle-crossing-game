from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager
import time

# Create the screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.title('Turtle Crossing Game')
screen.tracer(0)

# Create the player

player = Player()

# Create the cars

car_manager = CarManager()

# Create the scoreboard

scoreboard = Scoreboard()

# Listen to move player

screen.listen()
screen.onkey(fun=player.move, key='Up')

# Update screen
is_game_on = True
time_elapsed = 0
wait_time = 0.1

while is_game_on:
    time.sleep(wait_time)
    time_elapsed += 0.1
    screen.update()

    # Move the cars

    for car in car_manager.the_cars:
        car.move()

        # Detect car collision with wall

        car_manager.detect_wall_collision(car)

        # Detect player and car collision

        if player.distance(car) < 28:
            is_game_on = False
            scoreboard.game_over()

    # Add one more car

    if time_elapsed == 0.7 and len(car_manager.the_cars) <= 15:
        time_elapsed = 0
        car_manager.create_single_car()

    # Player completes the level

    if player.ycor() > 270:
        player.reset()
        scoreboard.level_up()
        wait_time *= 0.9
        car_manager.increase_speed()

# Click to close screen

screen.exitonclick()
