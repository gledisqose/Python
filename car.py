class Car():
    def __init__(self, make , model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' '+ self.make.title()+' '+self.model.title()
        return long_name

    def read_odometer(self):
        print("This car has "+ str(self.odometer_reading)+" miles on it!")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer!")

    def increment_odometer(self, mile):
        self.odometer_reading += mile


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + " kWh battery.")

    def upgrade_battery(self):
        print("The actual battery size is: "+str(self.battery_size)+" kWh")
        self.battery_size = 85
        print("The upgraded battery size is: " + str(self.battery_size) + " kWh")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()



my_tesla = ElectricCar('tela', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.upgrade_battery()