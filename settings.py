import logging
import tornado
import tornado.template
import os
from tornado.options import define, options

# Make filepaths relative to settings.
path = lambda root,*a: os.path.join(root, *a)
ROOT = os.path.dirname(os.path.abspath(__file__))

define("port", default=8000, help="run on the given port", type=int)
define("config", default=None, help="tornado config file")
tornado.options.parse_command_line()

MEDIA_ROOT = path(ROOT, 'media')
TEMPLATE_ROOT = path(ROOT, 'templates')

settings = {}
settings['static_path'] = MEDIA_ROOT
settings['xsrf_cookies'] = True
settings['template_loader'] = tornado.template.Loader(TEMPLATE_ROOT)
