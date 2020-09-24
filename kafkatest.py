import pywifi
from pywifi import const

wifi = pywifi.PyWiFi()
ifaces = wifi.interfaces()[0]
ifaces.scan()
bessis = ifaces.scan_results()

for data in bessis:
	print(data.ssid)

print(ifaces.status())
print(const.IFACE_CONNECTED, const.IFACE_CONNECTING)

# ifaces.disconnect()
# print(ifaces.status())

profile = pywifi.Profile()
profile.ssid = "jichengceshi_5G"
profile.auth = const.AUTH_ALG_OPEN
profile.akm.append(const.AKM_TYPE_WPA2PSK)
profile.cipher = const.CIPHER_TYPE_CCMP
profile.key = "Testwaiwang1234"
ifaces.remove_all_network_profiles()
tmp_profile = ifaces.add_network_profile(profile)
ifaces.connect(tmp_profile)
print("1234")