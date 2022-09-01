#!/usr/bin/env bash

for i in city amenity place review
do
	echo  "from models.base_model import BaseModel\nclass $i(BaseModel):\n"""Represent a $i Model"""'" >> models/$i.py
done
