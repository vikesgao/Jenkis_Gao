#coding=utf-8
from appium import webdriver
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0'
desired_caps['app'] = PATH('E:\Git_wbiao\helloGao\Jenkis_Gao\Jenkis_Gao\Package\myapp_unsigned_signed.apk')
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.wbiao.wbapp'
desired_caps['appActivity'] = 'com.wbiao.mall.welcome.WelcomeActivity'
# desired_caps['resetKeyboard'] = 'True'
# desired_caps['noReset'] = 'False'
# desired_caps['unicodeKeyboard'] = 'True'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)