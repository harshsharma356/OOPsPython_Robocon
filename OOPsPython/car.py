class Car:
    def __init__(self, model, year, color, ForSale):
        self.model = model
        self.year = year
        self.color = color
        self.ForSale = ForSale

    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"THe car is a {self.model} of year {self.year} of color {self.color}")