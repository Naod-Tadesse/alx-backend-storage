#!/usr/bin/env python3
"""
topic update
"""


import pymongo


def update_topics(mongo_collection, name, topics):
    """mongo update topic"""
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
