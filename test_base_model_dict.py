#!/usr/bin/python3
from models.base_model import BaseModel

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