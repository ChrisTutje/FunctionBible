class Car:
    def __init__(self, make=None, model=None, year=None):
        self._make = make
        self._model = model
        self._year = year

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, value):
        self._make = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    def drive(self):
        print(f"The {self.year} {self.make} {self.model} is now being driven.")

    def display(self):
        print(f"Car details: {self.year} {self.make} {self.model}")

