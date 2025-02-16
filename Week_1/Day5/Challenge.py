import math

class Circle():
    def __init__(self, radius= None, diameter = None):
        if radius is not None:
          self.radius = radius
        elif diameter is not None:
          self.radius = diameter / 2
        else:
            raise ValueError("Enter either radius or diameter")
       

    def area(self):
        area = math.pi * self.radius **2
        return area
    
    @property
    def radius(self):
        return f"The radius of the circle is equal to {self.radius}"

    def __str__(self):
       return f"The circle has {self.radius} cm  radius and {self.dimeter} as d'imater. "
    
    def __add__(self, other_circle):
        return self.radius + other_circle.radius
    
    def __gt__(self, other_circle):
        return self.radius == other_circle.radius
    
    def sort(self, liste,  *other_circle):
        liste.append(self)
        liste.append(*other_circle)
        liste.sort()
        return liste
        
import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        """
        Initialize a Circle object with either a radius or a diameter.
        If both are provided, radius takes precedence.
        If neither is provided, a ValueError is raised.
        """
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2  # Calculate radius from diameter
        else:
            raise ValueError("You must specify either a radius or a diameter.")

    def area(self):
        """
        Calculate and return the area of the circle using the formula: area = π * r².
        """
        return math.pi * self.radius ** 2

    def __str__(self):
        """
        Return a string representation of the Circle object.
        Displays the radius, diameter, and area of the circle.
        """
        return f"Circle with radius: {self.radius}"

    def __add__(self, other_circle):
        """
        Add two Circle objects by summing their radii.
        Returns a new Circle object with the combined radius.
        """
        new_radius = self.radius + other_circle.radius
        return Circle(radius=new_radius)

    def __gt__(self, other_circle):
        """
        Compare two Circle objects to check if the current circle is larger.
        Returns True if the current circle's radius is greater than the other circle's radius.
        """
        return self.radius > other_circle.radius

    def __eq__(self, other_circle):
        """
        Compare two Circle objects to check if they are equal.
        Returns True if both circles have the same radius.
        """
        return self.radius == other_circle.radius

    def __lt__(self, other_circle):
        """
        Compare two Circle objects to check if the current circle is smaller.
        Returns True if the current circle's radius is less than the other circle's radius.
        """
        return self.radius < other_circle.radius

    @staticmethod
    def sort_circles(circle_list):
        """
        Sort a list of Circle objects by their radius in ascending order.
        """
        circle_list.sort(key=lambda circle: circle.radius)
        return circle_list