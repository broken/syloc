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

@bottle.route('/a/<key>')
def album(key=''):
  return template('views/album.html', key=key)

@bottle.route('/master')
@bottle.route('/master/<filepath:path>')
def admin(filepath=''):
  return static_file('admin.html', root='views')

@bottle.route('/components/syloc/<filepath:path>')
def syloc(filepath):
  return static_file(filepath, root='components/syloc')

@bottle.route('/components/<filepath:path>')
def components(filepath):
  return static_file(filepath, root='bower_components')


# Define an handler for 404 errors.
@bottle.error(404)
def error_404(error):
  """Return a custom 404 error."""
  return 'Sorry, nothing at this URL.'
