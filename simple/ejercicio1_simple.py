"""
Hacer una función que genere una lista de diccionarios que contengan id y edad, donde
edad sea un número aleatorio entre 1 y 100 y la longitud de la lista sea de 10
elementos. retornar la lista.

Hacer otra función que reciba lo generado en la primer función y ordenarlo de mayor a
menor. Printear el id de la persona más joven y más vieja. Devolver la lista ordenada.

"""
import random

def create_people_list():
    people_list = []

    for i in range(1, 10+1):
        person = {
            "id": i,
            "edad": random.randint(1, 100)
        }
        people_list.append(person)

    return people_list

def create_sorted_list(people_list):

    ordered_list = sorted(people_list, key=lambda person: person["edad"])

    id_min_age = min(ordered_list, key=lambda person: person["edad"])["id"]
    id_max_age = max(ordered_list, key=lambda person: person["edad"])["id"]

    print(f"Persona mas joven id: {id_min_age}, persona mas vieja id: {id_max_age}")

    return ordered_list
     
           
people_list = create_people_list()
ordered_list = create_sorted_list(people_list)

print(ordered_list)

