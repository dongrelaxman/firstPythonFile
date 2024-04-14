class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self, increment):
        self.speed += increment

    def brake(self, decrement):
        self.speed -= decrement
        if self.speed < 0:
            self.speed = 0

    def get_speed(self):
        return self.speed


# Creating an instance of the Car class
my_car = Car("Toyota", "Camry", 2020)

# Accelerating the car
my_car.accelerate(20)

# Displaying the current speed
print("Current speed:", my_car.get_speed())

# Braking the car
my_car.brake(10)

# Displaying the current speed after braking
print("Current speed after braking:", my_car.get_speed())
