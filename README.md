## WALDO PHOTOS (TEST)
Test code for retrieving, parsing and ingesting images from waldo's s3 bucket.

### Instructions
#### Setting Up Stuff
To setup dependencies, either run `pip install -r requirements.txt` or setup a virtual environment.

#### Interaction
After setting up the environment and dependencies:
* To ingest the images metadata to db: `python main.py --action store`
-- _To extract and save extra features from the images, set the option `--extract true`_
* To query images:
-- The allowed search parameters are:
    * `--key [image_key]`
    * `--lastmodified [lastmodified data]`
    * `--etag [image_etag]`
    * If none of the above arguments is passed, all the images will be returned
* To remove all the photos from db: `python main.py --action remove`
* For help: `python main.py --help`