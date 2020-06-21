class vehicle:
    category = 'Car'

    def __init__(self,color,doors): #initializer
      """
      colors and  doors are instatance Attribute
      """

      self.color = color
      self.doors = doors
# instancing an object
rover = vehicle('red', '4')


# printing instance attribute
print(f"vehicle color: {rover.color}") 

#printing class attribure
print(f"Vehicle category: {rover.category}")
print(f"Vehicle doors: {rover.doors}")

#we can access the class attributes this way too
print(f"category:{rover.__class__.category}")
