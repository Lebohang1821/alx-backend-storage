#!/usr/bin/env python3
'''
Inserts a new doc in a collection based on kwargs'''


def insert_school(mongo_collection, **kwargs):
  '''Insert a new doc'''
  result = mongo_collection.insert_one(kwargs)
  return result.inserted_id
