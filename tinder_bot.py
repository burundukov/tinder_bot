from selenium import webdriver
import time


class TinderBot():

    def __init__(self):
        self.driver = webdriver.Chrome()
        #self.driver.implicitly_wait(10)

    def login(self):
        self.driver.get("https://tinder.com/")

        time.sleep(6)

        button = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[1]/div/button')
        button.click()

        time.sleep(4)

        new_window = self.driver.window_handles[1]
        first_window = self.driver.window_handles[0]

        self.driver.switch_to_window(new_window)

        email = self.driver.find_element_by_css_selector('#identifierId')
        email.send_keys('boyarilaa@gmail.com')

        a = self.driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
        a.click()

        # input password
        time.sleep(3)

        b = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        b.send_keys('ggim12345')
        c = self.driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
        c.click()

        time.sleep(3)
        button_5 = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[2]/button')
        button_5.click()
        time.sleep(1)
        button_6 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div[3]/div[2]/button')
        button_6.click()
        time.sleep(5)

    def alert_off(self):
        new_window = self.driver.window_handles[0]
        self.driver.switch_to_window(new_window)
        time.sleep(10)

        button_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        button_3.click()

        time.sleep(1)

        button_4 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        button_4.click()




    def like(self):
        button_like = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[4]/button')
        button_like.click()

    def dislike(self):
        pass



    def auto_like(self):
        while True:
            time.sleep(0.4)
            try:
                self.like()
            except:
                pass











bot = TinderBot()
bot.login()
bot.alert_off()

time.sleep(6)

bot.auto_like()
