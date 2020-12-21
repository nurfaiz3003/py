## Lambda
people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Faiz", "house": "Cianjur"},
    {"name": "Ujang", "house": "Slytherin"}
]

#   def f(person):
#       return person["house"]

people.sort(key=lambda person: person["name"])

print(people)