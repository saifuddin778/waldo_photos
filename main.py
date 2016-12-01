from pprint import pprint
from argparse import ArgumentParser as argp

from storage import storage


class main(object):

    def __init__(self, extract_image_exif=False):
        self.storage = storage(extract_image_exif=extract_image_exif)

    def store(self):
        self.storage.store()

    def remove(self):
        self.storage.truncate()

    def count(self):
        return self.storage.count()

    def query(self, key):
        data = self.storage.query(key)
        return data


if __name__ == "__main__":
    parser = argp(description="test code for waldo photos")
    parser.add_argument("-action",  "--action",  help="action needed", required=True, choices=["store", "remove", "count", "query"])
    parser.add_argument("-extract", "--extract", help="true if exif data to be extracted out of images", required=False)
    parser.add_argument("-key",     "--key",     help="image key to be queried", required=False)
    parser.add_argument("-lastmodified",     "--lastmodified",     help="image's lastmodified date to be queried", required=False)
    parser.add_argument("-etag",     "--etag",     help="image's etag to be queried", required=False)

    args = parser.parse_args()
    action = args.action
    extract_image_exif = args.extract

    if action == "query":
        data = main(extract_image_exif).query(args)
        for each in data:
            pprint(each)
    elif action == "store":
        main(extract_image_exif).store()
    elif action == "remove":
        main().remove()
    elif action == "count":
        count = main().count()
        print count
