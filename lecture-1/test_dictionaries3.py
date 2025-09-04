# Crea una lista de diccionarios
dogs=[
    {
    "name": "Yato", #name: clave, llave, atributo
    "sex": "male",
    "age": 6,
    "color": "golden"  
},

{
    "name": "Apolo",
    "sex":"male",
    "age":9,
    "color":"white"
}
]

dogs.append({
    "name":"Negro",
    "age":1,
    "sex":"male",
    "color":"black"
})

for item in dogs:
    #print(item["age"])
    print(item)

print(dogs[2])