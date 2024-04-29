#!/usr/bin/env python3
'''
It inserts new doc in collection based on kwargs'''


def insert_school(mongo_collection, **kwargs):
  '''It inserts new doc'''
  result = mongo_collection.insert_one(kwargs)
  return result.inserted_id
