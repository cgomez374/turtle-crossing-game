from turtle import Screen
from random import randint, choice
from player import Player
from scoreboard import Scoreboard
from car import Car
import time


# Create random coordinates for the cars

def create_random_coord():
    start_x = randint(280, 300)
    start_y = randint(-250, 250)
    return [start_x, start_y]


# Create a single car to add one by one

def create_single_car():
    colors = ['red', 'blue', 'yellow', 'green', 'orange', 'purple']
    rand_coord = create_random_coord()
    car_color = choice(colors)
    new_car = Car(car_color, rand_coord[0], rand_coord[1])
    return new_car


# Start the game with multiple cars

def create_multiple_cars():
    cars = []
    for i in range(3):
        cars.append(create_single_car())

    return cars


# Create the screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.title('Turtle Crossing Game')
screen.tracer(0)

# Create the player

player = Player()

# Create the cars

the_cars = create_multiple_cars()

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

    for car in the_cars:
        car.move(5)

        # Detect car collision with wall

        if car.xcor() < -280:
            new_coord = create_random_coord()
            car.reset(new_coord[0], new_coord[1])

        # Detect player and car collision

        if player.distance(car) < 28:
            is_game_on = False
            scoreboard.game_over()

    # Add one more car

    if time_elapsed == 0.7 and len(the_cars) <= 15:
        time_elapsed = 0
        the_cars.append(create_single_car())

    # Player completes the level

    if player.ycor() > 270:
        player.reset()
        scoreboard.level_up()
        wait_time *= 0.9





























# Click to close screen

screen.exitonclick()