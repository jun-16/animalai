from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

#APIキーの情報

key = "b71726e9e6c494536ac75dfa31d39b5c"
secret = "a3862b44cb4a92f5"
wait_time = 1

#保存フォルダの指定
animalname = sys.argv[1]
savedir = "./" + animalname

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
     text = animalname,
     per_page = 600,
     media = 'photos',
     sort = 'relevance',
     safe_search = 1,
     extras = 'url_q, licence'
)

photos = result['photos']
#戻り値を表示する
#pprint(photos)

for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath): continue
    urlretrieve(url_q,filepath)
    time.sleep(wait_time)
