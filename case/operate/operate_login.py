import requests
from setting.project_config import *


class OperateLogin(object):
    # 封装获取运营后台登录token的值

    @staticmethod
    def operate_land(phone_number, encrypted_password):
        # 在调用时请传入自己的手机号与加密密码

        url = operate_address+"/ddc-user-center/auth/login/pass"
        # 运营后台登录接口

        querystring = {
            "time": time_stamp,
            "sign": "zxcvbnmasdfghjkl",
            "phone": phone_number,
            "sysCode": "operate-management",
            "source": "pc",
            "password": encrypted_password,
            "app": "false"
        }

        payload = "{}"
        headers = {
            'Connection': "keep-alive",
            'Accept-Language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            'New-Ddc-Token': "",
            'Content-Type': "application/json",
            'Accept-Encoding': "gzip, deflate",
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:67.0) Gecko/20100101 Firefox/67.0",
            'Accept': "*/*",
            'Content-Length': "2"
        }

        response = requests.request(
            "POST", url, data=payload,
            headers=headers, params=querystring)
        print(response.text)

        if response.status_code == 200:
            logging.info("运营后台登录成功")
        else:
            logging.error("运营后台登录失败")

        return response.json()["data"]["token"]
    # 返回运营后台登录token的值

