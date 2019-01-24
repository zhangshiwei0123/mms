from appium import webdriver
def get_driver(app_package,app_activity):
    # server 启动参数
    desired_caps = {}
    # 设备信息 android不区分大小写
    desired_caps['platformName'] = 'Android'
    # 要和你自己测试手机版本对应上
    desired_caps['platformVersion'] = '5.1'
    # 设备名称值Android是可以随意写的
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # app信息
    desired_caps['appPackage'] = app_package
    desired_caps['appActivity'] = app_activity
    # 理解成是 手机的大管家
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)