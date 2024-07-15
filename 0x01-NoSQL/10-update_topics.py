#!/usr/bin/env python3
'''dfahtsykjyduluigl.,iutl
'''


def update_topics(mongo_collection, name, topics):
    '''zDhtrdsgu,ugjk.iogrjdgjhmtxuyktyr
    '''
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
