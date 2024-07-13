import asyncio
from kasa import SmartPlug

"""
7/10/24
Dar Govindan-
This function uses the Kasa Smart home package and uses the local network to control the smart plug. The IP may change at some point.
If this is the case, from Niels's macbook, just go to the terminal, and type the command "arp -a" and locate the ip address for the device with the mac address "A8:42:A1:7:85:77" and update the code accordingly
"""
async def light_control(status_change):
    p = SmartPlug("10.0.0.40")
    await p.update()
    if(status_change == "on"):
        await p.turn_on()
    elif(status_change == "off"):
        await p.turn_off()
    
def lightOn():
    asyncio.run(light_control("on"))
def lightOff():
    asyncio.run(light_control("off"))

lightOn();
