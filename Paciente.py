class Persona:
    def __init__(self,nombre, telefono, email) :
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
    
    def info (self):
        print ("El nombre del paciente es {}, su numero telefono es: {} y su email {}".format(self.nombre, self.telefono, self.email))

class Domicilio(Persona):
    def __init__(self, nombre, telefono, email, direccion, ciudad ):
        super().__init__(nombre, telefono, email)
        self.direccion = direccion 
        self.ciudad = ciudad
        
    def info(self):
        super().info()
        print ("La direccion del paciente es {}, {}".format(self.direccion, self.ciudad) )

class Profesion(Domicilio):
    def __init__(self, nombre, telefono, email, direccion, ciudad, profecion):
        super().__init__(nombre, telefono, email, direccion, ciudad)
        self.profecion = profecion
    
    def info(self):
        super().info()
        print ("La profesion del paciente es: {}".format(self.profecion))
        if self.profecion == "Estudiante":
            semestre = input ("Ingresa el semetre en que te encuentras:  ")
        elif self.profecion == "Profesor":
            semestre = input ("Ingresa de que institucion eres:  ")
        else:
            print ("Es persona externa")
    
paciente = Profesion ("Maria Lopez", "55 7867 9890", "marial@gmail.com","Calzada Ignacio", "Ciudad de Mexico", "Estudiante")

paciente.info()
paciente2 = Profesion ("Eduardo Martinez", "55 7989 3029", "Martinez@hotmail.com", "calle Paraiso", "Argentina", "Profesor")
paciente2.info()

