import json
import logging
from bottle import Bottle
from bottle import mako_template as template
from bottle import static_file
from gdata import geo
from gdata import media
from gdata.photos import service

bottle = Bottle()

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

@bottle.route('/')
def main():
  return static_file('main.html', root='views')

@bottle.route('/components/syloc/<filepath:path>')
def syloc(filepath):
  return static_file(filepath, root='components/syloc')

@bottle.route('/components/<filepath:path>')
def components(filepath):
  return static_file(filepath, root='bower_components')

@bottle.route('/a/<key>')
def album(key=''):
  # todo: get album id from key
  username = '117561345629918325267'
  album_id = key  # 5880506174047638001
  gd_client = service.PhotosService()
  photo_feed = gd_client.GetFeed('/data/feed/api/user/%s/albumid/%s?kind=photo' % (username, album_id))
  #photos = [photo_entry.media.content[0].url for photo_entry in photo_feed.entry]
  photos = []
  for photo_entry in photo_feed.entry:
    photo = { 'url': photo_entry.media.content[0].url,
               'id': photo_entry.gphoto_id.text,
          'summary': photo_entry.media.description.text }
    # Not adding thumbnail for now. Can have many differentiated by height
    if photo_entry.geo.Point.pos.text:
      photo['lat'] = photo_entry.geo.latitude()
      photo['long'] = photo_entry.geo.longitude()
    photos.append(photo)
  return template('views/album.html', photos=json.dumps(photos))


# Define an handler for 404 errors.
@bottle.error(404)
def error_404(error):
  """Return a custom 404 error."""
  return 'Sorry, nothing at this URL.'
