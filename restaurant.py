class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.onumber_served = 56

    def describe_restaurant(self):
        print("Restaurant name is " + self.restaurant_name.title())
        print("Cuisine type is " + self.cuisine_type.title())

    def open_restaurant(self):
        print("The restaurant is open!")

    def set_number_served(self):
        print("Number of customers that this restaurant has been served is: " + str(self.onumber_served))

    def increment_number_served(self, number):
        self.onumber_served += number


#restaurant = Restaurant('padam', 'italian')
#print("Resaturant name: " + restaurant.restaurant_name.title())
#print("Cuisine type: " + restaurant.cuisine_type.title())
#restaurant.describe_restaurant()
#restaurant.open_restaurant()
#restaurant.set_number_served()
#restaurant.increment_number_served(100)
#restaurant.set_number_served()