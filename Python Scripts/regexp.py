"""
. (dot) any character
\w word char
\d digit
\s whitespace
\S non-whitespace
"""
import re

def Find(pat, text):
    match = re.search(pat,text)
    if match:
        print(match.group())
    else: print('not found')

Find('iig', 'called piiig')

