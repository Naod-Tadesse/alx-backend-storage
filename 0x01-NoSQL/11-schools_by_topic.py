#!/usr/bin/env python3
"""
schools by topic
"""


import pymongo


def schools_by_topic(mongo_collection, topic):
    """specific topic of schools"""
    return mongo_collection.find({"topics": topic})
