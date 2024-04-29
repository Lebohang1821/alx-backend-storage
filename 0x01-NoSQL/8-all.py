#!/usr/bin/env python3
'''
Function lists all documents in a collcetion
'''


def list_all(mongo_collection):
  '''list all docs'''
  return [doc for doc in mongo_collection.find()]
