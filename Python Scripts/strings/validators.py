"""
Input Format

A single line containing a string .

Constraints


Output Format

In the first line, print True if  has any alphanumeric characters. Otherwise, print False. 
In the second line, print True if  has any alphabetical characters. Otherwise, print False. 
In the third line, print True if  has any digits. Otherwise, print False. 
In the fourth line, print True if  has any lowercase characters. Otherwise, print False. 
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
"""
def hasAlphaNum(string):
    return any(char.isalnum() for char in string)

def hasDigit(string):
    return any(char.isdigit() for char in string)

def hasAlpha(string):
    return any(char.isalpha() for char in string)

def hasCaps(string):
    return any(char.isupper() for char in string)

def hasLows(string):
    return any(char.islower() for char in string)


if __name__ == '__main__':
    #s = input()
    s="#$%@^&*kjnk svskjnbui h 4oi3hheuh /dfh uidshvhdsuihv suihc 0hrem89m4c02mw4xo;,wh fwhncoishmxlxfkjsahnxu83v 08 n8OHOIHIOMOICWHOFCMHEOFMCOEJMC0J09C 03J J3L;JMFC3JM3JC3'JIOO9MMJ099U N090N9 OOHOLNHNLLKNLKNKNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333000000000000000000000000000000000000000000000000000000000000000000000000000"
    out = []
    out.append(hasAlphaNum(s))
    out.append(hasAlpha(s))
    out.append(hasDigit(s))
    out.append(hasLows(s))
    out.append(hasCaps(s))
    print(*out, sep = "\n")
