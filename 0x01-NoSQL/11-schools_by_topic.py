#!/usr/bin/env python3
'''adrgsfgyjfikujlsdfgfhkj.
'''


def schools_by_topic(mongo_collection, topic):
    '''sfgjxfyjdstyuik7ilk75yuZDATsS
    '''
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(topic_filter)]
