class User:
    def __init__(self,usernamei,idi):
        self.username=usernamei
        self.__id=idi # Atributo privado
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,idi):
        try:
            self.__id=int(idi)
        except ValueError:
            print("Invalid ID format. ID must be an integer.")

u=User('felipe',"1234")
u.id="5678A"

print(u.id)