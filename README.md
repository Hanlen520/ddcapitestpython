# ddcapitestpython    
YYY接口自动化测试  

![目录图片](https://github.com/yjlch1016/ddcapitestpython/blob/master/resource/github_img.png)
  
# 一、数据驱动的思路      
1、采用requests+unittest+ddt+xlrd+pymysql+BeautifulReport   
2、requests是发起HTTP请求的第三方库     
3、unittest是Python自带的单元测试工具      
4、ddt是数据驱动的第三方库      
5、xlrd是读取Excel的第三方库    
6、pymysql是连接MySQL的第三方库    
7、BeautifulReport是生成Html测试报告的第三方库     

# 二、工程的目录结构      
1、case是测试用例包      
    case/app是预留给app的包      
    case/operate是预留给运营后台的包      
    case/store是预留给门店后台的包      
2、log是日志目录       
3、report是测试报告的目录     
4、resource是Excel预置数据文件的目录     
    用于存放用例名称、接口路径、各个字段与预期结果     
    resource/app/*文件名称.xlsx是app的      
    resource/operate/*文件名称.xlsx是运营的      
    resource/store/*文件名称.xlsx是门店的      
5、setting是工程的配置文件包       
6、tool是常用方法的封装类包      
7、run_all.py是工程的执行文件     

# 三、unittest的原理      
1、class MyTestCase(unittest.TestCass)是测试类名      
2、def setUpClass(cls)与def setUp(self)是测试用例运行前的准备方法        
    setUpClass(cls)方法在整个测试类中只运行一次     
2、def tearDownClass(cls)与def tearDown(self)是测试用例运行后的清理方法       
    tearDownClass(cls)在整个测试类中只运行一次     
3、def test_something(self)是测试方法的入口，测试用例即在里面写       
    以test_*开头命名，一个测试类可以有多个测试方法       
4、self.assertEqual(True, False)是断言       
    即判断实际结果与预期结果是否一致      

