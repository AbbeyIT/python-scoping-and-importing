class student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def introduce(self):
        print("Hi! " + self.name + " You're course is " + self.course)
