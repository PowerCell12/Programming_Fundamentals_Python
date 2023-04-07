class Circle:
    __pi = 3.14
    

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = self.diameter / 2

    def calculate_circumference(self):
        self.circumference = self.diameter * Circle.__pi
        return self.circumference

    def calculate_area(self):
        self.area = self.radius * self.radius  * Circle.__pi
        return self.area

    def calculate_area_of_sector(self, angle):
            self.area_sector = (angle / 360) * Circle.__pi * self.radius * self.radius
            return self.area_sector
