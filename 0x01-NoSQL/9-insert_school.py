#!/usr/bin/env python3
"""
new document
"""


import pymongo


def insert_school(mongo_collection, **kwargs):
    """new collection"""
    return mongo_collection.insert(kwargs)
