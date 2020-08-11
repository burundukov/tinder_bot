from selenium import webdriver
import time
import random



class TinderBot():

    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://tinder.com/")

        time.sleep(5)

        #убрать нижний футор

        button_close_1 = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[2]/button')
        button_close_1.click()
        time.sleep(8)
        button_close_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div[3]/div[2]/button')
        button_close_2.click()
        time.sleep(3)

        button_0 = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div[2]/div/div[2]/button').click()
        time.sleep(3)

        button = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[1]/div/button')
        button.click()

        time.sleep(4)

        new_window = self.driver.window_handles[1]

        self.driver.switch_to_window(new_window)

        # input email

        email = self.driver.find_element_by_css_selector('#identifierId')
        email.send_keys('boyarilaa@gmail.com')

        a = self.driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
        a.click()

        # input password
        time.sleep(6)

        b = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        b.send_keys('ggim12345')
        c = self.driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
        c.click()

        time.sleep(5)

    def alert_off(self):
        new_window = self.driver.window_handles[0]
        self.driver.switch_to_window(new_window)
        time.sleep(6)

        button_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        button_3.click()

        time.sleep(1)

        button_4 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        button_4.click()

    def like(self):
        button_like = self.driver.find_element_by_css_selector('#content > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div.recsCardboard.W\(100\%\).Mt\(a\).H\(100\%\)--s.Px\(10px\)--s.Pos\(r\) > div > div.Pos\(r\).Py\(16px\).Px\(4px\).Px\(8px\)--ml.D\(f\).Jc\(sb\).Ai\(c\).Maw\(375px\)--m.Mx\(a\).Pe\(n\).Mt\(-1px\) > div:nth-child(4)')
        button_like.click()

    def auto_like(self):
        while True:
            time.sleep(0.6)
            try:
                self.like()
                try:
                    link = self.driver.find_element_by_css_selector("#modal-manager > div > div > div > div > div.Pos\(r\).W\(100\%\) > a")
                    link.click()
                except:
                    continue

                try:
                        cansel = self.driver.find_element_by_xpath("//*[@id='modal-manager']/div/div/div[2]/button[2]")
                        cansel.click()
                except:
                        continue
            except:
                print("Получен лайк")
                time.sleep(3.4)
                try:
                    message_sended = self.driver.find_element_by_css_selector("#chat-text-area")
                    message_sended.send_keys(randomise())
                    button_sended = self.driver.find_element_by_xpath("//*[@id='modal-manager-canvas']/div/div/div[1]/div/div[3]/div[3]/form/button")
                    button_sended.click()
                    linck = self.driver.find_element_by_css_selector("#modal-manager-canvas > div > div > div.M\(a\).Expand.Pos\(r\).Flx\(\$flx1\).Pb\(36px\)--ml.Maw\(375px\)--ml.Mah\(620px\)--ml > div > div.Pos\(r\).W\(100\%\) > a")
                    linck.click()
                except:
                    print("тормозит интернет")




#message

def randomise():

    message_1 = ['Привет) ', 'Здравствуйте. ', 'Добрый день) ']
    message_2 = ['Вы мне очень симпатичны, очень хорошо выглядите) ', 'Вы такая красивая) ']
    message_3 = ['Только хочу сказать что я не любитель переписываться, я предпочитаю живое общение! Оставьте свой номер для связи',
                'Может перейдем в вотсапп, дадите свой номер?', 'Только сейчас я тороплюсь, оставте свой номер, чтобы я написал или позвонил?']
    message = random.choice(message_1) + random.choice(message_2) + random.choice(message_3)
    return message








bot = TinderBot()
bot.login()
bot.alert_off()
time.sleep(6)
bot.auto_like()
