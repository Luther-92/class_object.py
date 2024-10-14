"""
Think of it like designing your own "blueprints" (called classes) for objects in the real world.
Example: Imagine creating a blueprint for a car, 
and then using it to build different car objects like a red car, blue car, etc.

Inside a class, self lets you access the object's attributes (like brand and color) and methods (like drive()). 
Without self, the class wouldn’t know which object’s data to use.
"""
class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def call(self):
        print(f"Calling from {self.brand} {self.model}")

#create phone object
my_phone = Phone("Samsung", "S23")
my_phone.call()

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def play_song(self):
        print(f"Now playing: {self.title} by {self.artist} [{self.duration} minutes]")

#create song object
song1 = Song("Water", "Tyla", 4)
song1.play_song()

class Student:
    def __init__(self, name, grade, favorite_subject):
        self.name = name
        self.grade = grade
        self.favorite_subject = favorite_subject
        
    def study(self):
        print(f"{self.name} is studying {self.favorite_subject}.")
    def grade_up(self):
        self.grade += 1
        print(f"{self.name} has been promoted to grade {self.grade}!")

#create object for student
student1 = Student("Qhawe", 9, "English")
student2 = Student("Rayhan", 11, "Maths")

student1.study()
student2.grade_up()



