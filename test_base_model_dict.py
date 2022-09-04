#!/usr/bin/python3
from models.base_model import BaseModel

<<<<<<< HEAD
b = BaseModel()
b.name = "John"
b.age = 20
b.save()
b_json = b.to_dict()
print(b_json)
print('JSON of b:')
for key in b_json.keys():
        print("\t{}: ({}) - {}".format(key, type(b_json[key]), b_json[key]))

print('-----')
new_model = BaseModel(**b_json)
print(new_model.id)
print(new_model)
print(type(new_model.created_at))

print('--------')
print(b is new_model)
=======
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
>>>>>>> 90a30e0ddeccd71fcf6b90926aa9f27494d2bb19
