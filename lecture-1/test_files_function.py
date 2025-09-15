from json import dumps

def registerUser(name,id):
    # Abre archivo
    file=open('data/MY_DATA.txt','a')
    #file=open('C:/Users/samae/Documents/docencia-uq/II-2025/Programming/slides/lecture-1-sources/data/my_data.txt','a')
    
    data={"name":name,"id":id}
    
    # Escribe el texto en el archivo
    file.write(dumps(data)+'\n')
    
    # Cierra el archivo
    file.close()


