import json

import requests
from setting.project_config import *


class StoreLogin(object):
    # 封装获取门店登录token的值

    @staticmethod
    def store_land(phone_number, encrypted_password):
        # 在调用时请传入自己的手机号与加密密码

        url = store_address+"/auth/login"
        # 门店登录接口

        querystring = {
            "time": time_stamp,
            "sign": universal_signature
        }

        payload = {
            "mobile": phone_number,
            "password": encrypted_password
        }

        headers = {
            'accept': "application/json, text/plain, */*",
            'accept-encoding': "gzip, deflate",
            'accept-language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            'connection': "keep-alive",
            'content-length': "70",
            'content-type': "application/json",
            'new-ddc-token': "",
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:67.0) Gecko/20100101 Firefox/67.0",
        }

        response = requests.request(
            "POST", url, data=json.dumps(payload),
            headers=headers, params=querystring)
        # 用json.dumps()方法把data字典转换为合法的JSON字符串格式
        print(response.text)

        if response.status_code == 200:
            logging.info("门店登录成功")
        else:
            logging.error("门店登录失败")

        return response.json()["data"]["token"]
    # 返回门店登录token的值

