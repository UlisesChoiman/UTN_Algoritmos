
class Person:
    __slots__ = "__name", "__age"
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def set_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age > 0:
            self.__age
        else:
            return "Debe ingresar una edad valida"
    
persona_1 = Person("jose", 40)

persona_1.age = -23
persona_1.height = 1,90
print(persona_1.age)
print(persona_1.height)

#modificadores de acceso
#public in age ---> age = 20

# Public ---> Se puede acceder desde cualquier lado self.name.
# Private ----> Solo puede acceder la propia calse sel.__name
# Protected ----> Propiac clase y clases heredadas self._name
