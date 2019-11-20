class Car:
      
    # init method or constructor 
    def __init__(self, model, color): 
        self.model = model 
        self.color = color 
          
    def show(self): 
        print("Model is", self.model ) 
        print("color is", self.color )

    # both objects have different self which


# contain their attributes
audi = Car("audi a4", "blue")
ferrari = Car("ferrari 488", "green")

audi.show()  # same output as car.show(audi)
ferrari.show()  # same output as car.show(ferrari)


# Behind the scene, in every instance method
# call, python sends the instances also with
# that method call like car.show(audi)