class Circle :
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
        
    # Instance Method   
    def calculate_area(self):
        return Circle.pi * self.radius

    # Class Method - It cannot access - radius
    @classmethod
    def access_pi(cls):
        cls.pi = 3.1436
        
    # Static Method -  It cannot access - pi and radius
    @staticmethod
    def circle_static_method():
        print("This is circle's static method")
        
cir = Circle(5)