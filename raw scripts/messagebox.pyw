# Simple Messagebox
import ctypes  # An included library with Python install.
ctypes.windll.user32.MessageBoxA(None, "Your text", "Your title", 0)