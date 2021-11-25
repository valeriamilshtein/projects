'''
Urllib module is the URL handling module for python.
It is used to fetch URLs (Uniform Resource Locators).
It uses the urlopen function and is able to fetch URLs using a variety of different protocols.

Urllib is a package that collects several modules for working with URLs, such as:
* urllib.request for opening and reading
* urllib.robotparser for parsing robot.txt files
* urllib.parse for parsing URLs
* urllib.error for the exceptions raised.

Install 'pip install urllib' in Terminal.
'''

# This will import urlopen class from urllib module.
from urllib.request import urlopen

page = urlopen("https://mr-unity-buddy.hashnode.dev/")
print(page.headers)

# You can also see the coding of the website by using read() function.
# This will import urlopen class from urllib module.
from urllib.request import urlopen
page=urlopen("http://hashnode.com")

# Fetches the code of the web page.
content = page.read()
print(content)