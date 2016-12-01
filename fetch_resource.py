import requests
import xmltodict

from helpers import helpers
from config import(
    bucket_url,
    item_key,
    null_data
)


class fetch_resource(object):
    """streams the resource from s3 bucket"""

    def __init__(self):
        self.url = bucket_url
        self.key = item_key
        self.null = null_data
        self.key_maps = [
            ("Key",          helpers.null),
            ("LastModified", helpers.date_),
            ("Size",         helpers.int_),
            ("StorageClass", helpers.null),
            ("ETag",         helpers.str_)
        ]

    def _get_(self):
        """fetches all the images data"""

        resp = requests.get(self.url)
        if resp.status_code == 200:
            resp = resp.text
        else:
            resp = self.null
        return resp

    def map_keys(self, item):
        """maps values of image data to right type"""

        return dict((key.lower(), func(item[key])) for key, func in self.key_maps if key in item)

    def _fetch_(self):
        """entrypoint function to stream image resources"""

        rdata = self._get_()
        data = xmltodict.parse(rdata)
        for parent in data:
            for item in data[parent].get(self.key, []):
                yield self.map_keys(dict(item))
