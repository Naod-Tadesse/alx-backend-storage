#!/usr/bin/env python3
"""
document in collection
"""


import pymongo


def list_all(mongo_collection):
    """all docs in collection"""
    if not mongo_collection:
        return []
    docs = mongo_collection.find()
    return [doc for doc in docs]
