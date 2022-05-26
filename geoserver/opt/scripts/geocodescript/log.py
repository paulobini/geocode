#ESCRITO POR PAULO BINI 27-10-2021
import logging
from logging.handlers import RotatingFileHandler
import os

#DEFINIÇÕES DE LOG
rootpath = os.getcwd()
logfile = os.path.join(rootpath, "log/log.txt")
my_handler = RotatingFileHandler(logfile, mode='a', maxBytes=5*1024*1024, backupCount=4, encoding='utf-8', delay=0)
my_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
my_handler.setLevel(logging.INFO)
app_log = logging.getLogger()
app_log.setLevel(logging.INFO)
app_log.addHandler(my_handler)

def addlog(msg):
    app_log.info(msg)