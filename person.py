# Class
class Person:
    # class variables
    first_name: str  # public
    last_name: str   # public
    __age: int       # private
    
     # constructor
    def __init__(self, fname: str, lname: str, age: int) ->None:
        # instance variables
        self.first_name = fname
        self.last_name = lname
        self.__age = age
        return None
    
     # instance method
    def getAge(self) ->int:
        return self.__age
    
    def ageUp(self) ->None:
        self.__age += 1
        return None
    
    def getFullname(self) ->str:
        return "{} {}".format(self.first_name,self.last_name)
    
    def printFullname(self):
        print(self.getFullname())
