from behave import *
from base.BasePage import BasePage
from base.CommonFunction import CommonFunction
from pages.MainPage import MainPage
from pages.LoginPage import LoginPage
import config.config as config

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

@given('Chrome Browser로 NAVER URL에 접속한다.')
def step_impl(context):
    if not hasattr(context, 'driver'):
        options = Options()
        # ChromeDriver의 경로를 직접 지정합니다.
        service = Service('./config/chromedriver')
        # Service 객체를 사용하여 ChromeDriver의 경로를 전달합니다.
        context.driver = webdriver.Chrome(service=service, options=options)
        context.driver.get(config.BASE_URL)
        context.driver.implicitly_wait(5)

@given('테스트 수행에 필요한 초기화를 한다.')
def step_impl(context):
    context.bs = BasePage(context.driver)
    context.mp = MainPage(context.driver)
    context.lp = LoginPage(context.driver)

@given('창을 최대화한다.')
def step_impl(context):
    context.bs.maximize_window()
