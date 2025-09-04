# Ejemplo de diccionarios y conjuntos

from random import choice

# Citas disponibles
appointments=[
       {
       "doctor":354444,
       "patient": 14466,
       "date":"25/09/2025",
       "time":"8:00"       
       },
        {
       "doctor":143322,
       "patient": 569777,
       "date":"13/10/2025",
       "time":"13:00"       
       },
        {
       "doctor":354444,
       "patient": 789447,
       "date":"31/12/2025",
       "time":"23:59"       
       },
        {
       "doctor":143322,
       "patient": 45789636,
       "date":"2/1/2026",
       "time":"7:00"       
       },
]
    



# Conjunto de puestos de parqueo ocupados
doctor1Appointments=set()
doctor2Appointments=set()

doctor1ID=354444
doctor2ID=143322

for u in appointments:   
        match u["doctor"]:
                case 354444:
                        doctor1Appointments.add((u["date"],u["time"]))
                case 143322:
                        doctor2Appointments.add((u["date"],u["time"]))


print(doctor1Appointments)
print(doctor2Appointments)

