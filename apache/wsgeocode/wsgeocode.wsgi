import sys
import logging

sys.path.insert(0, '/var/www/wsgeocode')

logging.basicConfig(level=logging.warning,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='/var/log/apache2/wsgeocode/wsgi.log',
                    filemode='w')
logging.debug('A debug message')
logging.info('Some information')
logging.warning('A shot across the bows')

activate_this = '/var/www/.local/share/virtualenvs/wsgeocode-2uJauS1s/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from api import app as application