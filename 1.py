import os
import sys
from PIL import ImageGrab
import time

save_path = "D:\\1\\test1\\1.jpg";
cmd1 = "git add " + save_path
cmd2 = "git commit -m 'test'"
cmd3 = "git push origin master"


while(True):
    try:
        image = ImageGrab.grab()
        image.save(save_path)
        os.system(cmd1)
        os.system(cmd2)
        os.system(cmd3)
    except:
        pass
    time.sleep(300)
