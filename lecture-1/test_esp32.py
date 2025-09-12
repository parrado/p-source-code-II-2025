from json import loads

file=open('package_esp32_index.json')

esp32=file.read()
esp32d=loads(esp32)
print(esp32d["packages"][0]["name"])