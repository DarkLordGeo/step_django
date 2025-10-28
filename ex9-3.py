"""
9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.

Create several instances representing different users, and call both meth-
ods for each user.
"""


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(self.first_name, self.last_name)

    def greet_user(self):
        print(f"hello {self.first_name} {self.last_name}")


user_1 = User("John", "travota")
user_2 = User("Angelina", "Jolie")

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

