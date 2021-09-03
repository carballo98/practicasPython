from genericpath import exists
import os
from types import ClassMethodDescriptorType
CARPETA = 'contactos/'       #carpeta contactos
EXTENSION = '.txt'           #extensión del archivo
class Contacto:              #Contactos
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria
        
def app():
    
    crear_directorio()
    mostrar_menu()          #menu de opciones
    
    preguntar = True
    while preguntar:        #pregunta al usser la acción que desea realizar
        opcion = input('Seleccione una opción: \r\n')
        opcion = int(opcion)
        if opcion == 1:     #opciones
            agregar_nuevo_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
             print('Opción no valida, intente de nuevo por favor')
             
def mostrar_menu():  
    print('Seleccione del menú lo que desea hacer:')
    print('1) Agregar nuevo contacto')
    print('2) Editar contacto')
    print('3) Ver todos los contactos')
    print('4) Buscar contacto')
    print('5) Eliminar contacto')
    
def crear_directorio():
    if not os.path.exists('contactos/'):
        os.makedirs('contactos/') #creacion carpeta
    else:
        print('La carpeta ya existe')

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)


def buscar_contacto():
    nombre = input('Seleccione el contacto que desea buscar \r\n')
    try:
        with open (CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Información del contacto \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El archivo no existe')
        print(IOError)
    app()
             
def editar_contacto():
    print('Escribe el nombre del contacto que quiere editar')
    nombre_anterior = input('Nombre del contacto que desea editar: \r\n') 
    #Revisión de archivo
    existe = os.path.isfile(CARPETA + nombre_anterior + EXTENSION)
    
    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:
            #Campos
            nombre_contacto = input('Agrega el nuevo nombre \r\n')
            telefono_contacto = input('Agrega el nuevo teléfono \r\n')
            categoria_contacto = input('Agrega la nueva categoría \r\n')
            #Instancia
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            #Archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Teléfono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoría: ' + contacto.categoria + '\r\n')
            #Renombre archivo
        os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)
            
        print('\r\n Contacto editado correctamente \r\n')
            
    else:
        print('Ese contacto no existe')
             
def agregar_nuevo_contacto():
    print('Escribe los datos del nuevo contacto')
    nombre_contacto = input('Nombre del contacto:\r\n')
    
    #Revisión de archivo
    existe = os.path.isfile(CARPETA + nombre_contacto + EXTENSION)
    
    if not existe: 
    
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:
            archivo.write('Nombre: ' + nombre_contacto + '\r\n')
        #Resto de los campos
            telefono_contacto = input('Agrega el Telefono: \r\n')
            categoria_contacto = input('Categoría contacto: \r\n')
        
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)  #instancia de la clase
        #Escritura del archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Teléfono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoría: ' + contacto.categoria + '\r\n')
        
        #mensaje final exitoso
        print('\r\n Contacto creado correctamente \r\n')
    else:
        print('Este contacto ya existe')
        
    #Reinicio de los pedidos
    app()
    
    
def mostrar_contactos():
    archivos = os.listdir(CARPETA)
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]
    
    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                #imp contents
                print(linea.rstrip())
            print('\r\n')

def eliminar_contacto():
    nombre = input('Seleccione el contacto que desea eliminar: \r\n')
    
    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('\r\nEliminado correctamente!')
    except expression as identifier:
        print('No existe ese contacto')
        
    #Reset app
    
app()