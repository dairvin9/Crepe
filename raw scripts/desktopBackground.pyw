import ctypes
import os
drive = "C:\\"
folder = "Users\\Denise\\Documents\\GitHub\\ScriptKiddieStarterKit\\raw scripts"
image = "taylorSwiftFaceQuote.jpg"
image_path = os.path.join(drive, folder, image)
#image_path = '\\'.join([drive, folder, image])
print "woo"
print image_path
SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image_path, 3)