import unittest
import requests
from ddt import ddt, data

from case.operate.operate_login import OperateLogin
from setting.project_config import *
from tool.connect_mysql import ConnectMySQL


@ddt
class MarketingCouponList(unittest.TestCase):
    """
    营销中心
    根据券ID或名称查看优惠券，使优惠券生效、失效，删除优惠券的用例
    （共计5条）
    """

    @classmethod
    def setUpClass(cls):
        new_ddc_token = OperateLogin.operate_land(
            "13688888888", "123456")
        # 调用获取运营登录token

        cls.headers = {
            'Connection': "keep-alive",
            'Accept-Language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            'New-Ddc-Token': new_ddc_token,
            'Accept-Encoding': "gzip, deflate",
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:67.0) Gecko/20100101 Firefox/67.0",
            'Accept': "*/*",
        }

    @data(
        *ConnectMySQL.query_mysql("SELECT id FROM ddc_marketing_center.coupon_info WHERE coupon_status!=-1 AND created_by= '杨建良' ORDER BY RAND() LIMIT 1;"))
    def test_search_by_id(self, query_key):
        """
        根据优惠券ID查询优惠券的用例
        """

        url = operate_address+"/ddc-marketing-center/coupon"
        querystring = {
            "sign": "zxcvbnmasdfghjkl",
            "pageSize": "20",
            "pageNum": "1",
            "queryKey": query_key,
            "time": time_stamp
        }

        response = requests.request(
            "GET", url, headers=self.headers, params=querystring)

        actual_results = response.text
        expected_results = "\"code\":200000,\"message\":\"成功\""

        if expected_results in actual_results:
            logging.info("用例名称=根据优惠券ID查询优惠券的用例"+"=>执行通过")
        else:
            logging.error("用例名称=根据优惠券ID查询优惠券的用例"+"=>执行失败")

        self.assertIn(expected_results, actual_results)
        time.sleep(0.5)

    @data(
        *ConnectMySQL.query_mysql("SELECT coupon_name FROM ddc_marketing_center.coupon_info WHERE coupon_status!=-1 AND created_by= '杨建良' ORDER BY RAND() LIMIT 1;"))
    def test_search_by_name(self, query_key):
        """
        根据优惠券名称查询优惠券的用例
        """

        url = operate_address + "/ddc-marketing-center/coupon"
        querystring = {
            "sign": "zxcvbnmasdfghjkl",
            "pageSize": "20",
            "pageNum": "1",
            "queryKey": query_key,
            "time": time_stamp
        }

        response = requests.request(
            "GET", url, headers=self.headers, params=querystring)

        actual_results = response.text
        expected_results = "\"code\":200000,\"message\":\"成功\""

        if expected_results in actual_results:
            logging.info("用例名称=根据优惠券名称查询优惠券的用例"+"=>执行通过")
        else:
            logging.error("用例名称=根据优惠券名称查询优惠券的用例"+"=>执行失败")

        self.assertIn(expected_results, actual_results)
        time.sleep(0.5)

    @data(
        *ConnectMySQL.query_mysql("SELECT id FROM ddc_marketing_center.coupon_info WHERE coupon_status!=-1 AND send_type=0 AND created_by='杨建良' ORDER BY created_time DESC LIMIT 3,1;"))
    def test_delete_coupon(self, coupon_id):
        """
        删除优惠券的用例
        """
        coupon_id = " ".join('%s' % number for number in coupon_id)
        # 把元祖里面的int转换成str，然后再把元祖转换成字符串

        url = operate_address+"/ddc-marketing-center/coupon/"+coupon_id

        querystring = {
            "sign": "zxcvbnmasdfghjkl",
            "time": time_stamp
        }

        response = requests.request(
            "DELETE", url, headers=self.headers, params=querystring)

        actual_results = response.text
        expected_results = "\"code\":200000,\"message\":\"成功\""

        if expected_results in actual_results:
            logging.info("用例名称=删除优惠券的用例" + "=>执行通过")
        else:
            logging.error("用例名称=删除优惠券的用例" + "=>执行失败")

        self.assertIn(expected_results, actual_results)
        time.sleep(0.5)

    @data(
        *ConnectMySQL.query_mysql(
            "SELECT id FROM ddc_marketing_center.coupon_info WHERE coupon_status=0 AND created_by= '杨建良' ORDER BY created_time DESC LIMIT 2,1;"))
    def test_enable_coupon(self, coupon_id):
        """
        使优惠券生效的用例
        """
        coupon_id = " ".join('%s' % number for number in coupon_id)

        url = operate_address + "/ddc-marketing-center/coupon/enable/" + coupon_id

        querystring = {
            "sign": "zxcvbnmasdfghjkl",
            "time": time_stamp
        }

        response = requests.request(
            "PUT", url, headers=self.headers, params=querystring)

        actual_results = response.text
        expected_results = "\"code\":200000,\"message\":\"成功\""

        if expected_results in actual_results:
            logging.info("用例名称=使优惠券生效的用例" + "=>执行通过")
        else:
            logging.error("用例名称=使优惠券生效的用例" + "=>执行失败")

        self.assertIn(expected_results, actual_results)
        time.sleep(0.5)

    @data(
        *ConnectMySQL.query_mysql(
            "SELECT id FROM ddc_marketing_center.coupon_info WHERE coupon_status=1 AND created_by= '杨建良' ORDER BY created_time DESC LIMIT 2,1;"))
    def test_unable_coupon(self, coupon_id):
        """
        使优惠券失效的用例
        """
        coupon_id = " ".join('%s' % number for number in coupon_id)

        url = operate_address + "/ddc-marketing-center/coupon/unable/" + coupon_id

        querystring = {
            "sign": "zxcvbnmasdfghjkl",
            "time": time_stamp
        }

        response = requests.request(
            "PUT", url, headers=self.headers, params=querystring)

        actual_results = response.text
        expected_results = "\"code\":200000,\"message\":\"成功\""

        if expected_results in actual_results:
            logging.info("用例名称=使优惠券失效的用例" + "=>执行通过")
        else:
            logging.error("用例名称=使优惠券失效的用例" + "=>执行失败")

        self.assertIn(expected_results, actual_results)
        time.sleep(0.5)


if __name__ == '__main__':
    unittest.main()

