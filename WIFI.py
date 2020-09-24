import pywifi
import time
from pywifi import const

class wifi:
	def __init__(self):
		self.wifi = pywifi.PyWiFi()     #创建一个无线对象
		self.interfaces = self.wifi.interfaces()        #获取无线接口
		self.iface = self.interfaces[0]     #获取第一个无线网卡

	#获取无线网卡接口
	def get_wifi_interfaces(self):
		num = len(self.interfaces)
		if num <= 0:
			exit()
			return False
		if num == 1:
			return True

	# wifi连接
	def connect_wifi(self,wifi_name,wifi_password):
		# wifi扫描，获取需要连接wifi的加密类型
		wifi_akm = const.AKM_TYPE_WPA2PSK
		for data in self.iface.scan_results():
			if data.ssid == wifi_name:
				wifi_akm = data.akm

		# 判断是否已有wifi连接，若有则断开，没有就连接
		if self.iface.status() in [const.IFACE_CONNECTED,const.IFACE_CONNECTING]:
			print("已有WIFI连接")
			self.iface.disconnect()
			time.sleep(1)

		# wifi配置文件
		profile_info = pywifi.Profile()
		profile_info.ssid = wifi_name
		profile_info.auth = const.AUTH_ALG_OPEN
		profile_info.akm = wifi_akm
		profile_info.cipher = const.CIPHER_TYPE_CCMP
		profile_info.key = wifi_password
		# 删除所有连接过的wifi文件
		self.iface.remove_all_network_profiles()
		# 设置新的wifi配置文件
		tep_profile = self.iface.add_network_profile(profile_info)
		# wifi连接
		self.iface.connect(tep_profile)

		time.sleep(5)
		if self.iface.status() == const.IFACE_CONNECTED:
			print('\n==========================================================================')
			print('wifi：{0}连接成功，密码：{1}'.format(wifi_name, wifi_password), end='')
			print('==========================================================================\n')
			return True
		else:
			print("密码错误：{}".format(wifi_password),end='')
			return false

	def disconnect_wifi(self):
		self.iface.disconnect()
		time.sleep(1)

if __name__ == '__main__':
    wifi = wifi()
    wifi.connect_wifi("jichengceshi_5G","Testwaiwang1234")
