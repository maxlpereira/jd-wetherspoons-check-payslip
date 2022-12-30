from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PayslipBot:
    def __init__(self, employee, password, day, month, year, answer1, answer2):
        self.employee = employee
        self.password = password
        self.day = int(day + 1)
        self.month = int(month + 1)
        self.year = int(year - 20)
        self.answer1 = answer1
        self.answer2 = answer2
        self.driver = webdriver.Chrome(executable_path='chromedriver')
        self.driver.get("https://saas.zellis.com/jdw/dashboard/dashboard-ui/index.html#/landing")
    def login(self):
        username = self.driver.find_element(By.XPATH, '//*[@id="username"]')              
        username.click()
        username.send_keys(str(self.employee))
        username.send_keys(Keys.TAB)
        password = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        password.send_keys(str(self.password))
        password.send_keys(Keys.RETURN)
    def securityquentions(self):
        day = self.driver.find_element(By.XPATH, f'//*[@id="dobDay"]/option[{self.day}]')
        day.click()
        month = self.driver.find_element(By.XPATH, f'//*[@id="dobMonth"]/option[{self.month}]')
        month.click()
        year = self.driver.find_element(By.XPATH, f'//*[@id="dobYear"]/option[{self.year}]')
        year.click()
        try:
            answer = self.driver.find_element(By.XPATH, '//*[@id="answer01000001"]')
            answer.click()
            answer.send_keys(str(self.answer1))
        except:
            answer = self.driver.find_element(By.XPATH, '//*[@id="answer01000002"]')
            answer.click()
            answer.send_keys(str(self.answer2))
        finally:
            answer.send_keys(Keys.RETURN)
        
    def checknew(self):
        try:
            new_payslip = self.driver.find_element(By.CLASS_NAME, 'unread')
            return True
        except:
            return False
    



