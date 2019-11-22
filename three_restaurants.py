from restaurant import Restaurant

"""class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant name is " + self.restaurant_name.title())
        print("Cuisine type is " + self.cuisine_type.title())

    def open_restaurant(self):
        print("The restaurant is open!")

restaurant = Restaurant('padam', 'italian')
print("Resaturant name: " + restaurant.restaurant_name.title())
print("Cuisine type: " + restaurant.cuisine_type.title())
restaurant.describe_restaurant()
restaurant.open_restaurant()"""


first_restaurant = Restaurant('padam', 'italian')
second_restaurant = Restaurant('artigano', 'french')

first_restaurant.describe_restaurant()
second_restaurant.describe_restaurant()
