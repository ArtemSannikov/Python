import os
import sys
import webbrowser

from PIL import ImageGrab

dir_desktop = os.chdir('D:\Desktop')
print(os.getcwd())

screen = ImageGrab.grab()

screen.save('screenshot.png','PNG')

screen.show()
