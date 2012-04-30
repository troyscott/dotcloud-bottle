import os

from bottle import route, run
from bottle import static_file

htdocs = '%s/pub' % os.getcwd()


@route('/hello')
def hello():
	return 'Hello world'


@route('/')
def index():
	filename = 'index.html'
	return static_file(filename, root=htdocs)

@route('/<filename>')
def server_static(filename):
	return static_file(filename, root=htdocs)

