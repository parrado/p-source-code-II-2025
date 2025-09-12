from json import dumps

# Abre archivo con manejo de excepción
try:
    
    # Crea archivo my_data.txt
    file=open('data/my_data.txt','x')

    y=25.3
    x=y/0


    # Solicita datos al usuario
    name=input('Ingrese su nombre: ')
    id=int(input('Ingrese su cédula: '))

    data={"name":name,"id":id}

    # Escribe el texto en el archivo
    file.write(dumps(data)+"\n")

    # Cierra el archivo
    file.close()

except:
    # El bloque except se ejecuta si hay 
    # excepción, el archivo ya existe
    if file:
        file.close()
    print('El archivo ya existe')


