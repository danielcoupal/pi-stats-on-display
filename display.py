from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1309, ssd1325, ssd1331, sh1106, sh1107, ws0010
from time import sleep
import psutil

serial = i2c(port=1, address=0x3C)

device = sh1106(serial)

cpu_percent = psutil.cpu_percent()
cpu_load = psutil.getloadavg()[0]
mem_usage = psutil.virtual_memory()
disk_usage = psutil.disk_usage("/")
temperature = psutil.sensors_temperatures().get("cpu_thermal", [{"current": 0}])[0].current

with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((0, 0), f"CPU: {cpu_percent:.1f}% Load: {cpu_load:.2f}", fill=255)
    draw.text((0, 10), f"Mem: {mem_usage}", fill=255)
    draw.text((0, 20), f"Disk: {disk_usage}", fill=255)
    draw.text((0, 30), f"Temp: {temperature:.1f}°C", fill=255)

sleep(10)

