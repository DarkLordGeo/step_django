"""
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
"""


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name, self.cuisine_type)

    def open_restaurant(self):
        print("Restaurant is open")


rest = Restaurant("Kakhelebi", "Megruli")
rest2 = Restaurant("Megrelebi", "Kakhuri")
rest3 = Restaurant("Bikentia", "Kebab")

print(rest.restaurant_name, rest.cuisine_type)
print(rest2.restaurant_name, rest2.cuisine_type)
print(rest3.restaurant_name, rest3.cuisine_type)
