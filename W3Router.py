from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

class W3Router:
	def __init__(self):
		self.driver = webdriver.Chrome("C:\python 3.7.3\Scripts\chromedriver.exe")
		self.url = "http://wifi.ys7.com"

	def Login(self):
		self.driver.get(self.url)
		self.driver.maximize_window()
		sleep(5)
		# try:
		# 	self.driver.find_element_by_xpath("//*[@id='welcome_btn']").click()
		# 	sleep(3)
		# 	self.driver.find_element_by_xpath("//*[@id='next']").click()
		# 	sleep(3)
		# 	self.driver.find_element_by_id("usrpwd").send_keys("1234qwer")
		# 	self.driver.find_element_by_id("usrpwd2").send_keys("1234qwer")
		# 	self.driver.find_element_by_css_selector("#next").click()
		# except NoSuchElementException:
		# 	raise ValueError
		try:
			user_id = (By.ID,"userpwd")
			user_id_input = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(user_id))
			user_id_input.send_keys("1234qwer")

			self.driver.find_element_by_id("login_btn").click()
		except NoSuchElementException:
			raise ValueError

	def Choose_Mode(self,mode):
		try:
			switch = {"wired_uplink":"//*[@id='wired_uplink']","5g_up":"//*[@id='5g_up']"}
			mode_str = (By.XPATH,switch[mode])
			mode_click = WebDriverWait(self.driver,3).until(EC.visibility_of_element_located(mode_str))
			mode_click.click()
		except NoSuchElementException:
			raise ValueError

	def Setting_Mesh(self,up_ssid,up_pwd,mesh_ssid,mesh_pwd):
		try:
			ssid_desc = (By.XPATH,"//*[@id='ssid_desc']")
			ssid_desc_click = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(ssid_desc))
			ssid_desc_click.click()

			# 获取搜索到的上行5G数量,根据输入所需要连接是SSID进行搜索，搜索到之后选择
			sleep(3)
			sum_up_5G = self.driver.find_element_by_xpath("/html/body/div[3]/div[4]/ul")
			list = sum_up_5G.find_elements_by_xpath("li")
			i = 1
			count = 0
			for i in range(1,len(list)):
				up_5G = self.driver.find_element_by_xpath("/html/body/div[3]/div[4]/ul/li["+ str(i) +"]/div").text
				if up_ssid == up_5G and i < len(list):
					self.driver.find_element_by_xpath("/html/body/div[3]/div[4]/ul/li["+ str(i) +"]/div").click()
					self.driver.find_element_by_id("wifi_ok").click()
					break

			up_pwd_str = (By.ID,"ssid_pwd_input")
			up_pwd_str_input = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(up_pwd_str))
			up_pwd_str_input.send_keys(up_pwd)

			mesh_ssid_str = (By.XPATH,"//*[@id='2g_ssid']/div/input")
			mesh_ssid_str_input = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(mesh_ssid_str))
			mesh_ssid_str_input.send_keys(mesh_ssid)

			mesh_pwd_str = (By.XPATH,"//*[@id='2g_pwd']/div/div[1]/input")
			mesh_pwd_str_input = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(mesh_pwd_str))
			mesh_pwd_str_input.send_keys(mesh_pwd)
		except NoSuchElementException:
			raise ValueError

if __name__ == '__main__':
    W3R = W3Router()
    W3R.Login()
    W3R.Choose_Mode("5g_up")
    W3R.Setting_Mesh("jichengceshi_5G","Testwaiwang1234","Mesh_111","1234qwer")