import arrow
import exifread

from helpers import (
    helpers,
    null_support
)


class exif_data(object):
    """parses exif data out of the image"""

    def __init__(self):
        self.picked_keys = [
            ("Image DateTime",              helpers.date_),
            ("Image PrimaryChromaticities", helpers.null),
            ("Image Orientation",           helpers.str_),
            ("MakerNote FlashActivity",     helpers.str_),
            ("MakerNote ImageSize",         helpers.str_),
            ("MakerNote LensType",          helpers.str_),
            ("EXIF ExifImageWidth",         helpers.str_),
            ("Image Make",                  helpers.str_),
            ("MakerNote ModelID",           helpers.str_),
            ("Image Artist",                helpers.str_),
            ("MakerNote SpotMeteringMode",  helpers.str_),
            ("Image GPSInfo",               helpers.str_),
        ]
        pass

    def get_exif(self, saved, file_loc, image):
        """exif extractor (uses exifread library)"""

        if saved:
            try:
                img = open(file_loc, "rb")
                tags = exifread.process_file(img)
                img.close()
                for key, func in self.picked_keys:
                    val = tags.get(key, null_support)
                    new_key = key.replace(" ", "_").lower()
                    image[new_key] = func(val.printable)
            except Exception, e:
                print e
                pass
        return image
