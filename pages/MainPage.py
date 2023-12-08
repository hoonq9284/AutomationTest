from base.BasePage import BasePage
import pages.PageElements as pe

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_search_field(self):
        BasePage.is_displayed(self, pe.naver_search_field)

    def check_account_container(self):
        BasePage.is_displayed(self, pe.account_container)

    def check_login_info_text(self):
        BasePage.is_displayed(self, pe.login_info_text)

    def check_login_button(self):
        BasePage.is_displayed(self, pe.login_button)

    def check_find_id_text(self):
        BasePage.is_displayed(self, pe.login_find_id)

    def check_find_password_text(self):
        BasePage.is_displayed(self, pe.login_find_password)

    def check_register_text(self):
        BasePage.is_displayed(self, pe.login_register)

    def click_login_button(self):
        BasePage.click_element(self, pe.login_button)

    def check_login_page_logo(self):
        BasePage.is_displayed(self, pe.login_page_logo)

    def click_cafe_icon(self):
        BasePage.click_element(self, pe.service_icon_type_cafe)
        BasePage.switch_to_window(self)
        
    def check_cafe_logo(self):
        BasePage.is_displayed(self, pe.cafe_main_logo)
        title = self.driver.title
        BasePage.assert_text(title, pe.cafe_title)

    def click_blog_icon(self):
        BasePage.click_element(self, pe.service_icon_type_blog)
        BasePage.switch_to_window(self)

    def check_blog_logo(self):
        BasePage.is_displayed(self, pe.blog_main_logo)
        title = self.driver.title
        BasePage.assert_text(title, pe.blog_title)

    def click_shopping_icon(self):
        BasePage.click_element(self, pe.service_icon_type_shopping)
        BasePage.switch_to_window(self)

    def check_shopping_logo(self):
        BasePage.is_displayed(self, pe.shopping_main_logo)
        title = self.driver.title
        BasePage.assert_text(title, pe.shopping_title)

    def click_news_icon(self):
        BasePage.click_element(self, pe.service_icon_type_news)
        BasePage.switch_to_window(self)

    def check_news_logo(self):
        BasePage.is_displayed(self, pe.news_main_logo)
        title = self.driver.title
        BasePage.assert_text(title, pe.news_title)

    def click_stock_icon(self):
        BasePage.click_element(self, pe.service_icon_type_stock)
        BasePage.switch_to_window(self)

    def check_stock_logo(self):
        BasePage.is_displayed(self, pe.stock_main_logo)
        title = self.driver.title
        BasePage.assert_text(title, pe.stock_title)

    def click_real_icon(self):
        BasePage.click_element(self, pe.service_icon_type_real)
        BasePage.switch_to_window(self)

    def check_real_logo(self):
        BasePage.is_displayed(self, pe.real_main_logo)
        title = self.driver.title
        BasePage.assert_text(title, pe.real_title)

    def click_map_icon(self):
        BasePage.click_element(self, pe.service_icon_type_map)
        BasePage.switch_to_window(self)

    def check_map_logo(self):
        BasePage.is_displayed(self, pe.map_main_logo)
        title = self.driver.title
        BasePage.assert_text(title, pe.map_title)

    def click_webtoon_icon(self):
        BasePage.click_element(self, pe.service_icon_type_webtoon)
        BasePage.switch_to_window(self)

    def check_webtoon_logo(self):
        BasePage.is_displayed(self, pe.webtoon_main_logo)
        title = self.driver.title
        BasePage.assert_text(title, pe.webtoon_title)

    def check_top_aside_menu(self):
        BasePage.is_displayed(self, pe.top_aside_menu)

    def check_top_pay_menu(self):
        BasePage.is_displayed(self, pe.top_pay_menu)

    def check_top_talk_menu(self):
        BasePage.is_displayed(self, pe.top_talk_menu)

    def check_top_noti_menu(self):
        BasePage.is_displayed(self, pe.top_noti_menu)
        
        