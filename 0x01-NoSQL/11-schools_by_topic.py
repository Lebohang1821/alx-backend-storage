#!/usr/bin/env python3
'''
It returns lists of schools
'''


def schools_by_topic(mongo_collection, topic):
  '''It list schools having specified topic'''
  topic_filter = {
    'topics': {
      '$elemMatch': {
        '$eq': topic,
      },
    },
  }
  return [doc for doc in mongo_collection.find(topic_filter)]
