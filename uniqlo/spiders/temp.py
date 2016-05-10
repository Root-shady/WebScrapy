
import urllib
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def store_image_local(url):
    """
    Take in a image url, download the image, then return the local path where 
    the image is stored
    """
    image = urllib.urlretrieve(url, filename)

