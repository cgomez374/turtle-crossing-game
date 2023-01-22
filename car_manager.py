from car import Car
from random import randint, choice


class CarManager(Car):
    def __init__(self):
        self.the_cars = []
        self.start_x = 300
        self.start_y = 250

        self.create_random_coord()
        self.create_multiple_cars()

    # Create random coordinates for the cars

    def create_random_coord(self):
        self.start_x = randint(280, 300)
        self.start_y = randint(-250, 250)

    # Create a single car to add one by one

    def create_single_car(self):
        colors = ['red', 'blue', 'yellow', 'green', 'orange', 'purple']
        self.create_random_coord()
        car_color = choice(colors)
        new_car = Car(car_color, self.start_x, self.start_y)
        self.the_cars.append(new_car)

    # Start the game with multiple cars

    def create_multiple_cars(self):
        for i in range(3):
            self.create_single_car()

    def detect_wall_collision(self, car):
        # Detect car collision with wall

        if car.xcor() < -280:
            self.create_random_coord()
            car.reset(self.start_x, self.start_y)

    def increase_speed(self):
        for car in self.the_cars:
            car.move_dist += 5



