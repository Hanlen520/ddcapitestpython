import json
import random
import unittest

import ddt
import requests
from case.operate.operate_login import OperateLogin
from setting.project_config import *
from tool.read_excel import ReadExcel
from datetime import datetime, timedelta


@ddt.ddt
class MarketingCouponCreate(unittest.TestCase):
    """
    营销中心_新建优惠券的用例（共计36条）
    """

    @classmethod
    def setUpClass(cls):
        new_ddc_token = OperateLogin.operate_land(
            "13688888888", "123456")
        # 调用获取运营登录token

        cls.headers = {
            'accept': "*/*",
            'accept-encoding': "gzip, deflate",
            'accept-language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            'connection': "keep-alive",
            'content-length': "660",
            'content-type': "application/json",
            'new-ddc-token': new_ddc_token,
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:67.0) Gecko/20100101 Firefox/67.0",
        }

    @ddt.data(*ReadExcel.open_excel(
        excel_path + "/operate/create_coupon.xlsx", "Sheet1"))
    @ddt.unpack
    def test_create_coupon(
            self, case_name, interface_path,
            send_type, business_limits,
            collar_use_limit_everyday, collar_use_limit_everyone,
            discount_limit_status, coupon_rule_full,
            user_grant_limits, user_use_limits, expected_results):
        """
        运营新建优惠券
        """

        url = operate_address+interface_path

        querystring = {
            "time": time_stamp,
            "sign": "zxcvbnmasdfghjkl"
        }

        business_limits = str(business_limits)
        business_limits = business_limits.split(",")
        # 把business_limits字符串转为列表
        while "" in business_limits:
            business_limits.remove("")
            # 删除空值

        random_string = str(random.randint(100000, 999999))
        tomorrow = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')

        payload = {
            "budgetCode": random_string,
            "couponDescribe": "杨建良的券描述"+random_string,
            "couponEndTime": tomorrow,
            "couponInventory": "100",
            "couponName": "杨建良的券名称"+random_string,
            "sendType": int(send_type),
            "couponRule": {
                "availableTimeLimits": {
                    "availableEndTime": tomorrow,
                    "availableStartTime": today,
                    "validityDays": ""
                },
                "businessLimits": business_limits,
                "collarUseLimits": {
                    "collarUseLimitEveryday": collar_use_limit_everyday,
                    "collarUseLimitEveryone": collar_use_limit_everyone
                },
                "couponId": "",
                "discountLimitStatus": discount_limit_status,
                "discountLimits": {
                    "couponRuleFull": coupon_rule_full,
                    "couponRuleReduce": ""
                },
                "userGrantLimits": int(user_grant_limits),
                "userUseLimits": int(user_use_limits)
            },
            "couponStartTime": today,
            "couponTags": "杨建良的券标签"+random_string,
            "couponType": "1",
            "couponValue": "0.01"
        }

        response = requests.request(
            "POST", url, data=json.dumps(payload),
            headers=self.headers, params=querystring)
        actual_results = response.text
        # 实际结果

        if expected_results == actual_results:
            logging.info("用例名称={}".format(case_name)+"=>执行通过")
        else:
            logging.error("用例名称={}".format(case_name)+"=>执行失败")
        self.assertEqual(expected_results, actual_results)
        time.sleep(0.5)


if __name__ == '__main__':
    unittest.main()

