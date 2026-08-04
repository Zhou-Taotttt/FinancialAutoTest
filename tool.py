# 公共工具

import json
import logging
import time
from selenium import webdriver
from logging import handlers

from selenium.webdriver.chrome.service import Service

from config import PATH

class Tools:
    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            path=r'D:\develop\Python\Python312\chromedriver.exe'
            ser = Service(executable_path=path)
            cls.driver = webdriver.Chrome(service=ser)
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            time.sleep(2)
            cls.driver.quit()
            cls.driver=None

def read_json(file_name):
    data=[]
    file_path=PATH+'/data/'+file_name
    with open(file_path,mode='r',encoding='utf-8') as f:
        tmp=json.load(f)
        for i in tmp:
            a=tuple(i.values())
            data.append(a)
        return data

class GetLog:
    __log=None
    @classmethod
    def get_log(cls):
        if cls.__log is None:
            cls.__log=logging.getLogger()
            cls.__log.setLevel(logging.INFO)
            filename=PATH+'/log/'+'web.log'
            tf=logging.handlers.TimedRotatingFileHandler(filename,when='MIDNIGHT',interval=1,backupCount=3,encoding='utf-8')
            fmt='%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)]-%(message)s'
            fm=logging.Formatter(fmt)
            tf.setFormatter(fm)
            cls.__log.addHandler(tf)
        return  cls.__log
# 调试
if __name__=='__main__':
    Tools.get_driver().get('http://121.43.169.97:8081/')