#!/usr/bin/env python3
'''cb,jmvjhkhfcvhjkx
'''

def top_students(mongo_collection):
    '''xjvhdcjghlgjfhklgulogilio
    '''
    students = mongo_collection.aggregate(
        [
            {
                '$project': {
                    '_id': 1,
                    'name': 1,
                    'averageScore': {
                        '$avg': {
                            '$avg': '$topics.score',
                        },
                    },
                    'topics': 1,
                },
            },
            {
                '$sort': {'averageScore': -1},
            },
        ]
    )
    return students
