from bson import ObjectId
from pymongo import MongoClient

from helpers import helpers
from config import (
    mongouri,
    collection_
)


class db(object):
    """db object to interact with data store"""

    def __init__(self):
        self.mongouri = mongouri
        self.client = self.get_client(self.mongouri)
        self.collection_ = collection_
        self.allowed_keys = [
            ("key",          helpers.vnull),
            ("lastmodified", helpers.date_),
            ("etag",         helpers.vnull),
        ]
        pass

    def get_client(self, mongouri):
        """returns mongoclient"""

        client = MongoClient(mongouri)
        return client

    def ingest_(self, data):
        """ingests data to db collection"""

        self.client.renewable_energy_2015[self.collection_].save(data)

    def count_(self):
        """returns count of items in db collection"""

        return self.client.renewable_energy_2015[self.collection_].count()

    def remove_all(self):
        """truncates the db collection"""

        self.client.renewable_energy_2015[self.collection_].remove({})

    def query(self, args):
        """queries the db"""

        q = {}
        args = args.__dict__
        for key, func in self.allowed_keys:
            if key in args and args[key]:
                val = func(args[key])
                q[key] = val
        return [each for each in self.client.renewable_energy_2015[self.collection_].find(q)]
