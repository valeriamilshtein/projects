'''
The same gems can be used in Python programs too.

Install 'pip install emoji' in Terminal.
'''

from emoji import emojize

print(emojize(":laptop:"))

# Alternatively, encode() function can be used from emojis module to convert Unicode to emojis.
import emojis

emojified = emojis.encode("There is a :snake: in my boot!!!")
print(emojified)