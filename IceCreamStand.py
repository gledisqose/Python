from restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, iceCream_flavours):
        super().__init__(restaurant_name, cuisine_type)
        self.iceCream_flavours = iceCream_flavours

    def flavours(self):
        print("Ice cream flavours: "+ self.iceCream_flavours.title())

my_flavours = IceCreamStand(iceCream_flavours='banana')
