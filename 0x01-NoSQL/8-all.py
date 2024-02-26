#!/usr/bin/env python3
"""This Python function lists all documents in a collection:
"""


import pymongo


def list_all(mongo_collection):
    """Returns a list of all documents in collection"""
    if not mongo_collection:
        return []
    docus = mongo_collection.find()
    return [doc for doc in docus]
