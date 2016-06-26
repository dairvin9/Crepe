"""import ctypes
import os
#drive = "C:\\"
#folder = "Users\\Denise\\Documents\\GitHub\\ScriptKiddieStarterKit\\raw scripts"
#image = "taylorSwiftFaceQuote.jpg"
#image_path = os.path.join(drive, folder, image)
#image_path = '\\'.join([drive, folder, image])
image_path="C:\\Users\\Denise\\Documents\\GitHub\\ScriptKiddieStarterKit\\raw scripts\\taylorSwiftFaceQuote.jpg"
#image_path="\\taylorSwiftFaceQuote.jpg"
SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image_path, 3)"""
import ctypes
image_path="C:\\Users\\Denise\\Documents\\GitHub\\ScriptKiddieStarterKit\\raw scripts\\taylorSwiftFaceQuote.jpg"
SPI_SETDESKWALLPAPER = 20
fWinIni = 3
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image_path, fWinIni)

