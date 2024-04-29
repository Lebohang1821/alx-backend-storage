#!/usr/bin/env python3
'''
Change school topic
'''


def update_topics(mongo_collection, name, topics):
  '''changes all topics of a school doc'''
  mongo_collection.update_many(
    {'name': name},
    {'$set': {'topics': topics}}
  )
