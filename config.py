# 项目配置

import os
from faker import Faker

# 获取项目路径
PATH=os.path.dirname(__file__)
# 项目地址
BASE_URL='http://121.43.169.97:8081'
BACK_URL='http://121.43.169.97:8082'
# 人的信息
fk=Faker(locale='zh_CN')
NAME=fk.name()
PHONE=fk.phone_number()
CARD=fk.ssn()