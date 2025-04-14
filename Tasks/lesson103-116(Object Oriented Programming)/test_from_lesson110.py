class Car:
    def __init__(self, type, company, model):
        self.type = type
        self.company = company
        self.model = model
        print(f'your vehicle is a car and type is {self.type} and company is {self.company}')


bmw_khalid = Car('sedan', 'bmw', 'x6')


# print(bmw_khalid.model)

class Plane(Car):
    def __init__(self, type, company, model):
        super().__init__(type, company, model)
        print(f'your vehicle is plane and type is {self.type} and company is {self.company}')


khalid_plane = Plane('Airbus', 'Emirates', 'a1')
