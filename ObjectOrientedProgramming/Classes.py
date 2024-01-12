class Class:
    def __init__(self, attribute = None):  # default constructor
        self._attribute = attribute  # properties/attributes

    @property  # Getter
    def attribute(self):
        return self._attribute

    @attribute.setter  # Setter
    def attribute(self, value):
        self._attribute = value

    def method(self):  # Method
        return None

    def display(self):  # Display Method
        print(f"attribute: {self.attribute}")


#defaultInstance = Class()   # instantiation with default constructor
#defaultInstance.display()

#defaultInstance = Class(attribute = "something")   # instantiation with argument
#defaultInstance.display()