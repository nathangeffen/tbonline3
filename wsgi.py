import os
import sys

from django.core.handlers.wsgi import WSGIHandler

# Add the project path to the system path
sys.path.append('/home/tbonline/tb_prod/tbonline')
sys.path.append('/home/tbonline/tb_prod/tbonline/tbonlineproject')
sys.path.append('/home/tbonline/python2')
# sys.path.append('/home/tbonline/python2/external')

os.environ['DJANGO_SETTINGS_MODULE'] = 'tbonline.tbonlineproject.settings'
application = WSGIHandler()
