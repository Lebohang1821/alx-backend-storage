#!/usr/bin/env python3
'''
Returns lists of school
'''


def schools_by_topic(mongo_collection, topic):
  '''List of school having a specified topic'''
  topic_filter = {
    'topics': {
      '$elemMatch': {
        '$eq': topic,
      },
    },
  }
  return [doc for doc in mongo_collection.find(topic_filter)]
