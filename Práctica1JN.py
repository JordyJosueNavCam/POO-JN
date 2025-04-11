class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad



if __name__ =='__main__':
    oPersona1 = Persona('Jordy', 'Navarrete', edad=19)
    print(f'Nombre: {oPersona1._nombre}')
    print(f'Apellido: {oPersona1._apellido}')
    print(f'Edad: {oPersona1._edad}')