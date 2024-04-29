#!/usr/bin/env python3
'''
It changes schools topic
'''


def update_topics(mongo_collection, name, topics):
  '''It changes * topics of schools doc'''
  mongo_collection.update_many(
    {'name': name},
    {'$set': {'topics': topics}}
  )
