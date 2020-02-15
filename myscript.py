import time
def fan(device,width,height):
    device.swipe(width/2,height/2,0,height/2,0.2)
    time.sleep(1)
    device.swipe(0,height/2,width/2,height/2,0.2)