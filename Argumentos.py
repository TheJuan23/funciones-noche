def my_funcion (country = "colombia"):
    print("i am from "+ country)
my_funcion("sweden")
my_funcion("India")
my_funcion()
my_funcion("Brazil")

#argumentos arbitarios
def mostrarEstudiantes(*args):

    print("el estudiante: "+ args[2])
mostrarEstudiantes("Emil","Tobias","Linus")

def mostrarCarros(carro1, carro2, carro3):


    print("el carro es: " + carro2)
mostrarCarros("BMW","Ferrari","Mazda")

def mostrarCliente(**kwargs):

    print("su nombre es: "+ kwargs["apellido"])
mostrarCliente(nombre = "tobias", apellido = "Refsnes")