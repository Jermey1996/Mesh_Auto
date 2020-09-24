from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep

class Tplink_Stress:
	def __init__(self):
		self.driver = webdriver.Chrome("C:\python 3.7.3\Scripts\chromedriver.exe")
		self.url = "http://tplogin.cn/"

	def login(self,timeout = 10):
		self.driver.get(self.url)
		self.driver.maximize_window()
		sleep(5)
		try:
			password = self.driver.find_element_by_id("lgPwd")
			# password_input = WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(password))
			password.send_keys("1234qwer")
			self.driver.find_element_by_id("loginSub").click()
			sleep(5)
		except NoSuchElementException:
			raise ValueError

	def To_WIFI_Settings_Views(self,timeout = 10):
		try:
			self.driver.find_element_by_class_name("menu4").click()
			sleep(3)
			self.driver.find_element_by_xpath("//*[@id='wireless2G_rsMenu']/label").click()
			# Wifi_input = WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(Wifi))
			sleep(3)
		except NoSuchElementException:
			raise ValueError("找不到设置页面")

	def Drop(self):
		# self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
		scroll = self.driver.find_element_by_xpath("//*[@id='routeSetRConniceScrollSb1600336788857']/label")
		ActionChains(self.driver).drag_and_drop_by_offset(scroll,0,300).perform()

	def Select_Channel(self,channel):
		try:
			self.driver.find_element_by_id("channel").click()
			# sel = self.driver.find_element_by_class_name("selOptsUl")
			# Select(sel).select_by_visible_text("5")
			sleep(3)
			switch = {"自动":"//*[@id='selOptsUlchannel']/li[1]","1":"//*[@id='selOptsUlchannel']/li[2]",
			          "2":"//*[@id='selOptsUlchannel']/li[3]","3":"//*[@id='selOptsUlchannel']/li[4]",
			          "4":"//*[@id='selOptsUlchannel']/li[5]","5":"//*[@id='selOptsUlchannel']/li[6]"}

			switch_5G = {"自动":"//*[@id='selOptsUlchannel5g']/li[1]","36":"//*[@id='selOptsUlchannel5g']/li[2]",
			          "40":"//*[@id='selOptsUlchannel5g']/li[3]","44":"//*[@id='selOptsUlchannel5g']/li[4]",
			          "48":"//*[@id='selOptsUlchannel5g']/li[5]","149":"//*[@id='selOptsUlchannel5g']/li[6]",
			          "153":"//*[@id='selOptsUlchannel5g']/li[7]","157":"//*[@id='selOptsUlchannel5g']/li[8]",
			          "161":"//*[@id='selOptsUlchannel5g']/li[9]","165":"//*[@id='selOptsUlchannel5g']/li[10]"}
			self.driver.find_element_by_xpath(switch[channel]).click()
		except NoSuchElementException:
			raise ValueError
		# self.driver.find_element_by_id("save").click()

	def Set_SSID_PWD(self,ssid,pwd):
		try:
			# 设置SSID、密码参数
			ssid_input = self.driver.find_element_by_id("ssid")
			pwd_input = self.driver.find_element_by_id("wlanPwd")
			ssid_input.clear()
			ssid_input.send_keys(ssid)
			pwd_input.clear()
			pwd_input.send_keys(pwd)
		except NoSuchElementException:
			raise ValueError

if __name__ == '__main__':
	t = Tplink_Stress()
	t.login()
	t.To_WIFI_Settings_Views()
	t.Set_SSID_PWD("1234","1234qwer")
	# t.Drop()
	t.Select_Channel("3")

