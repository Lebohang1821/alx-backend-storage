#!/usr/bin/env python3
'''
It lists * documents in collcetion
'''


def list_all(mongo_collection):
  '''It shows * docs'''
  return [doc for doc in mongo_collection.find()]
