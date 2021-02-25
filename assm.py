import json
from PIL import Image

def getDevicesList():
	with open('./devicesArrays.json', encoding='utf-8') as f:
		raw = f.read()

		return(json.loads(raw))

if __name__ == '__main__':
	devicesList = getDevicesList()

	for device in devicesList:
		device_w = devicesList[device][0]
		device_h = devicesList[device][1]
		device_r = round(device_w / 5)

		image_w_center = round((device_w / 2) - (device_r / 2))
		image_h_center = round((device_h / 2) - (device_r / 2))
		
		base_image = Image.new('RGB', (device_w, device_h), (255, 255, 255))
		logo_image = Image.open('./logo.png')
		a = logo_image.resize((device_r, device_r))
		base_image.paste(a, (image_w_center, image_h_center),  a)
		base_image.save('./images/splash-portrait-{width}x{height}.png'.format(
		width=device_w, height=device_h))
