class Vehicle:

    def __init__ (self, maker, model, year, color):
        self.maker = maker
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0
        self.gear = 1
        self.max_gear = 4

    
    def change_speed (self, additional_speed):
        self.speed += additional_speed
        if self.speed < 0:
            self.speed = 0

    def accelerate (self, acceleration):
        self.change_speed (self.speed + acceleration)

    def brake (self, decceleration):
        self.change_speed (self.speed - decceleration)

    def choose_gear (self, chosen_gear):
        self.gear =+ chosen_gear
        if self.gear < 1:
            self.gear = 1
        elif self.gear > self.max_gear:
            self.gear = self.max_gear

    def increase_gear (self, additional_gear):
        self.chage_gear (self.gear + additional_gear)

    def decrease_gear (self, additional_gear):
        self.chage_gear (self.gear - additional_gear)


class Car(Vehicle):
    def __init__ (self,maker, model, year, color):
        super().__init__(maker,model, year, color)
        self.speed = 0
        self.gear = 1
        self.max_gear = 4

     
class Motorcycle(Vehicle):
      def __init__ (self,maker, model, year, color):
        super().__init__(maker,model, year, color)
        self.speed = 0

      def choose_gear(self, chosen_gear):
        pass

      def increase_gear(self, additional_gear):
        pass

      def decrease_gear(self, additional_gear):
        pass


class Truck(Vehicle):
      def __init__ (self,maker, model, year, color):
        super.__init__(maker,model, year, color)
        self.speed = 0
        self.gear = 1
        self.max_gear = 4

class UserInput():
        def __init__ 




print("Hello, what type of vehicle would you like to create?\n"
      "Choose 1\n"
      "If you would like to get a CAR, press  ---> 1\n"
      "If you would like to get a MOTORCYCLE, press  ---> 2\n"
      "If you would like to get a Truck, press  ---> 3")

choice = print(int(input("Please make your choice 1, 2 or 3")))

while True:
    if choice == 1:
        maker = print(input("Please enter vehicle's maker: "))
        model = print(input("Please enter your vehicle's color: "))
        year = print(int(input("Please enter the year of the vehicle: ")))
        colour = print(input("Please enter your vehicle's color: "))

    user_car = Car(maker, model, year, colour)


    if choice == 2:
        maker = print(input("Please enter motorcycle's maker: "))
        model = print(input("Please enter your motorcycle's color: "))
        year = print(int(input("Please enter the year of the motorcycle: ")))
        colour = print(input("Please enter your motorcycle's color: "))

    user_motorcycle = Motorcycle(maker, model, year, colour)

    if choice == 3:
        maker = print(input("Please enter truck's maker: "))
        model = print(input("Please enter your truck's color: "))
        year = print(int(input("Please enter the year of the truck: ")))
        colour = print(input("Please enter your truck's color: "))

    user_truck = Truck(maker, model, year, colour)






