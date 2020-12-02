class dog:
    """ a simple attemp to model a dog"""

    def __init__(self, name, age):
        """initialize name and age attributes"""
        self.name = name
        self.age = age 

    def sit(self):
        """simulate a dog response to sitting"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """simulate rolling over of a dog in response to a command"""
        print(f"{self.name} rolled over")
        

my_dog = dog('willie', 6)
my_dog.sit()
my_dog.roll_over()

print(f"my dog's name is {my_dog.name} .")
print(f"my dog's age is {my_dog.age}")