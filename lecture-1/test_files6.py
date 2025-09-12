from json import loads
# Combinación de bloques try/except con with
try:
    archiveName=input('Ingrese el nombre del archivo: ')
    file=open('data/'+archiveName)

except FileNotFoundError:
    print('El archivo no existe')
else:
    with file:
        # Lee todas las líneas del archivo
        # como una lista.
        lines=file.readlines()        
        
        users=[]
        # Imprime las líneas del archivo
        for l in lines:
            users.append(loads(l))
        
        print(users)
        print(users[0]['name'])