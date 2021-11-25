'''
Use the incessant flow of knowledge with Python for daily needs.

Install 'pip install wikipedia' in Terminal.
'''

import wikipedia

result = wikipedia.page("Python Programming Language")
print(result.summary)