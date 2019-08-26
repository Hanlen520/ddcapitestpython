import json
import unittest
import ddt
import requests
from case.store.store_login import StoreLogin
from setting.project_config import *
from tool.read_excel import ReadExcel


@ddt.ddt
# 声明使用ddt
class StoreCashier(unittest.TestCase):
    """
    门店收银的测试用例（共计10条）
    """

    @classmethod
    def setUpClass(cls):

        new_ddc_token = StoreLogin.store_land(
            "13688888888", "123456")
        # 调用获取门店登录token

        cls.headers = {
            'accept': "application/json, text/plain, */*",
            'accept-encoding': "gzip, deflate",
            'accept-language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            'connection': "keep-alive",
            'new-ddc-token': new_ddc_token,
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:67.0) Gecko/20100101 Firefox/67.0",
        }
        # 请求头cls.headers与self.header都是本类的公共属性

    @ddt.data(*ReadExcel.open_excel(
        excel_path+"/store/membership_code.xlsx", "Sheet1"))
    @ddt.unpack
    def test_membership_code(
            self, case_name, interface_path,
            membership_code, expected_results):
        """
        门店手动输入会员码
        """
        url = store_address+interface_path
        querystring = {
            "sign": universal_signature,
            "userCode": membership_code,
            "time": time_stamp
        }
        response = requests.request(
            "GET", url, headers=self.headers, params=querystring)
        actual_results = response.text
        # 实际结果

        if expected_results in actual_results:
            logging.info("用例名称={}".format(case_name)+"=>执行通过")
        else:
            logging.error("用例名称={}".format(case_name)+"=>执行失败")

        self.assertIn(expected_results, actual_results)
        time.sleep(0.5)

    @ddt.data(*ReadExcel.open_excel(
        excel_path+"/store/commodity_code.xlsx", "Sheet1"))
    @ddt.unpack
    def test_commodity_code(
            self, case_name, interface_path,
            commodity_code, expected_results):
        """
        门店手动输入商品编码
        """
        url = store_address+interface_path
        querystring = {
            "sign": universal_signature,
            "commodityEanCode": commodity_code,
            "time": time_stamp
        }

        response = requests.request(
            "GET", url, headers=self.headers, params=querystring)
        actual_results = response.text
        # 实际结果

        if expected_results in actual_results:
            logging.info("用例名称={}".format(case_name)+"=>执行通过")
        else:
            logging.error("用例名称={}".format(case_name)+"=>执行失败")

        self.assertIn(expected_results, actual_results)
        time.sleep(0.5)

    @ddt.data(*ReadExcel.open_excel(
        excel_path + "/store/push_order.xlsx", "Sheet1"))
    @ddt.unpack
    def test_push_order(
            self, case_name, interface_path,
            count, expected_results):
        """
        门店推送订单给顾客
        """
        url = store_address+interface_path
        querystring = {
            "time": universal_signature,
            "sign": time_stamp
        }
        count = str(count)
        payload = {
            "userId": "5c35a4e9fc238ea8e850cdefe10f1aaf",
            "skuList": [{
                "productName": "SKU商品描述45357",
                "barcode": "DDC5345312343",
                "skuId": "SKU5243513478",
                "spec": "",
                "color": "白色",
                "leftStoreNum": 1000,
                "salePrice": 0.01,
                "totalPrice": 10,
                "specification": "白色,",
                "count": count
            }]
        }
        self.headers['content-type'] = "application/json"

        response = requests.request(
            "POST", url, data=json.dumps(payload),
            headers=self.headers, params=querystring)
        actual_results = response.text
        # 实际结果

        if expected_results in actual_results:
            logging.info("用例名称={}".format(case_name)+"=>执行通过")
        else:
            logging.error("用例名称={}".format(case_name)+"=>执行失败")

        self.assertIn(expected_results, actual_results)
        time.sleep(0.5)


if __name__ == '__main__':
    unittest.main()

