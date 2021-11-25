'''
The pyperclip module has copy() and paste() functions that can
send a text to and receive text from your computer’s clipboard.
Python program to demonstrate pyperclip module.

Install 'pip install pyperclip' in Terminal.
'''

# This will import pyperclip.
import pyperclip

pyperclip.copy("Hello, everyone!")
pyperclip.paste()

pyperclip.copy("This is an interesting module!")
pyperclip.paste()