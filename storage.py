import os
import shutil
import requests

from db import db
from exif_data import exif_data
from fetch_resource import fetch_resource
from config import (
    temp_location,
    bucket_url
)


class storage(object):
    """
    - ingests the data from resource to db
    - also (optionally), extracts the exif data from image file if told so
    """

    def __init__(self, extract_image_exif):
        self.temp_location = temp_location
        self.bucket_url = bucket_url
        self.fetch_obj = fetch_resource()._fetch_
        self.exif_data = exif_data()
        self.db = db()
        self.extract_image_exif = extract_image_exif
        pass

    def download(self, url, filename, save_loc):
        """downloads the image file"""

        downloaded = False
        resp = requests.get(self.bucket_url + url, stream=True)
        if resp.status_code == 200:
            with open(save_loc, "wb") as f:
                resp.raw.decode_content = True
                shutil.copyfileobj(resp.raw, f)
            downloaded = True
        return downloaded

    def save(self, url):
        """saves the image file to disk for exif extraction"""

        filename = url
        save_loc = self.temp_location + filename
        saved = self.download(url, filename, save_loc)
        return saved, save_loc

    def remove(self, saved, save_loc):
        """removes the file from disk post exif extraction"""

        if saved:
            os.remove(save_loc)
        return

    def store(self):
        """reads from the stream, (optionally) extracts exif, and ingests to db"""

        print "beginning to store images.."

        n = 0
        #--iterate over the web resource
        for image in self.fetch_obj():
            #--if internal image exif data is to be extracted
            #--then download, extract exif and remove image
            if self.extract_image_exif:
                saved, save_loc = self.save(image["key"])
                image = self.exif_data.get_exif(saved, save_loc, image)
                self.remove(saved, save_loc)

            self.db.ingest_(image)
            print "%s processed...saved.. (#%d)" % (image["key"], n)
            n += 1
        return

    def count(self):
        """returns count of existing resource in db"""

        return self.db.count_()

    def truncate(self):
        """removes existing resource from db"""

        print "truncating the db"
        self.db.remove_all()

    def query(self, key):
        result = self.db.query(key)
        return result
