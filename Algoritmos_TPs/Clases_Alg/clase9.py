
# metodos por convencion para acceder a atributos privados getter y setter

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

#persona_1.age = -23
#persona_1.height = 1,90
#print(persona_1.age)
#print(persona_1.height)

#modificadores de acceso
#public in age ---> age = 20

# Public ---> Se puede acceder desde cualquier lado self.name.
# Private ----> Solo puede acceder la propia calse sel.__name
# Protected ----> Propiac clase y clases heredadas self._name

#get optenemos (retornamo) el valor del atributo
#set setiamos (asignamos) el valor del atributo

#Herencia ---> Permite heredar atributos a metodos

class Animal:
    def __init__(self, pelo, numero_de_patas, edad ):
        self.pelo = pelo
        self.numero_de_patas = numero_de_patas
        self.edad = edad
    
    def caminar(self):
        print("Animal caminando")

    def sonido(self):
        print("Animal haciendo sonido de animal")

#class Gato(Animal):
#    pass

#gato_1 = Gato("corto", 4, 30)

#print(gato_1.pelo)


class Gato(Animal):
    def __init__(self, name, pelo, numero_de_patas, edad):
        super().__init__(pelo, numero_de_patas, edad)
        self.name = name

gato_1 = Gato("corto", 4, 7, "lanita")
print(gato_1.pelo)
